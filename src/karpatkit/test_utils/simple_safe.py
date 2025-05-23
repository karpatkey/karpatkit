from dataclasses import dataclass

from eth_account.signers.local import LocalAccount
from gnosis.eth import EthereumClient, EthereumNetwork
from gnosis.safe import Safe, addresses
from hexbytes import HexBytes
from web3 import Web3
from web3.types import TxParams, TxReceipt

from defabipedia.types import Chain
from karpatkit.constants import Address


class SafeExecutionFailure(Exception):
    pass


@dataclass
class TxResult:
    tx_hash: HexBytes
    tx_params: TxParams
    receipt: TxReceipt


class SimpleEthereumClient(EthereumClient):
    def __init__(self, w3):
        self.w3 = w3


class SimpleSafe(Safe):
    """A simple Safe with one signer to be used in tests"""

    def __init__(self, address, w3: Web3, signer_key):
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
            safe_tx_gas=5_000_000,
            base_gas=5_000_000,
            gas_price=1,
            gas_token=Address.ZERO,
            refund_receiver=Address.ZERO,
        )
        safe_tx.sign(self.signer_key)
        tx_hash, _ = safe_tx.execute(self.signer_key)
        receipt = self.ethereum_client.get_transaction_receipt(tx_hash, timeout=60)

        for log in receipt["logs"]:
            for topic in log["topics"]:
                if topic == HexBytes("0x23428b18acfb3ea64b08dc0c1d296ea9c09702c09083ca5272e64d115b687d23"):
                    raise SafeExecutionFailure()
        return TxResult(tx_hash, safe_tx, receipt)

    @classmethod
    def build(cls, owner: LocalAccount, w3: Web3) -> "SimpleSafe":
        ethereum_client = SimpleEthereumClient(w3)
        network = EthereumNetwork(ethereum_client.w3.eth.chain_id)
        ethereum_tx_sent = cls.create(
            ethereum_client,
            deployer_account=owner,
            master_copy_address=addresses.MASTER_COPIES[network][0][0],
            owners=[owner.address],
            threshold=1,
            # using a proxy factory address as without it
            # the gas estimation is too high because of a bug in gnosis/safe/safe.py
            proxy_factory_address=addresses.PROXY_FACTORIES[network][1][0],
        )

        safe = SimpleSafe(ethereum_tx_sent.contract_address, w3, signer_key=owner.key)
        return safe
