from dataclasses import dataclass

from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from safe_eth.eth import EthereumClient, EthereumNetwork
from safe_eth.safe.addresses import MASTER_COPIES, PROXY_FACTORIES
from safe_eth.safe.safe import SafeV141
from safe_eth.safe.safe_creator import SafeCreator
from web3 import Web3
from web3.types import TxParams, TxReceipt

from defabipedia.types import Chain


class SafeExecutionFailure(Exception):
    pass


@dataclass
class TxResult:
    tx_hash: HexBytes
    tx_params: TxParams
    receipt: TxReceipt


class SimpleEthereumClient(EthereumClient):
    def __init__(self, w3: Web3):
        self.w3 = w3


class SimpleSafe(SafeV141):
    """A simple Safe with one signer to be used in tests"""

    def __new__(cls, address: ChecksumAddress, w3: Web3, signer_key: str):
        instance = super().__new__(cls, address, SimpleEthereumClient(w3))
        return instance

    def __init__(self, address: ChecksumAddress, w3: Web3, signer_key: str):
        self.signer_key = signer_key
        super().__init__(address, SimpleEthereumClient(w3))

    def send(self, txs) -> TxResult:
        from roles_royce.utils import multi_or_one  # TODO: refactor out from here

        tx = multi_or_one(txs, Chain.get_blockchain_from_web3(self.w3))
        safe_tx = self.build_multisig_tx(
            to=tx.contract_address,
            value=tx.value,
            data=tx.data,
            operation=tx.operation,
        )
        safe_tx.sign(self.signer_key)
        tx_hash, *_ = safe_tx.execute(self.signer_key)
        receipt = self.ethereum_client.get_transaction_receipt(tx_hash, timeout=60)
        for log in receipt["logs"]:
            for topic in log["topics"]:
                if topic == HexBytes("0x23428b18acfb3ea64b08dc0c1d296ea9c09083ca5272e64d115b687d23"):
                    raise SafeExecutionFailure()
        return TxResult(tx_hash, safe_tx, receipt)

    @classmethod
    def build(cls, owner: LocalAccount, w3: Web3) -> "SimpleSafe":
        ethereum_client = SimpleEthereumClient(w3)
        network = EthereumNetwork(ethereum_client.w3.eth.chain_id)
        ethereum_tx_sent = SafeCreator.create(
            ethereum_client=ethereum_client,
            deployer_account=owner,
            master_copy_address=MASTER_COPIES[network][0][0],
            owners=[owner.address],
            threshold=1,
            proxy_factory_address=PROXY_FACTORIES[network][0][0],
        )
        return cls(ethereum_tx_sent.contract_address, w3, signer_key=owner.key)
