from ..types import Chain, ContractSpec, parent


class ArbitrumContractSpecs:
    arb_sys = ContractSpec(
        address="0x0000000000000000000000000000000000000064",
        abi_path=parent(__file__) / "arb_sys.json",
        name="arb_sys",
    )


class EthereumContractSpecs:
    delayed_inbox = ContractSpec(
        address="0x4Dbd4fc535Ac27206064B68FfCf827b0A60BAB3f",
        abi_path=parent(__file__) / "delayed_inbox.json",
        name="delayed_inbox",
    )
    outbox4 = ContractSpec(
        address="0x0B9857ae2D4A3DBe74ffE1d7DF045bb7F96E4840",
        abi_path=parent(__file__) / "outbox4.json",
        name="outbox4",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.ARBITRUM: ArbitrumContractSpecs}
