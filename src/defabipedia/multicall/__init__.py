from defabipedia.types import Chain, ContractSpec, parent



class EthereumContractSpecs:
    MultiSend = ContractSpec(
        address="0xeefBa1e63905eF1D7ACbA5a8513c70307C1cE441",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )


class GnosisContractSpecs:
    MultiSend = ContractSpec(
        address="0xb5b692a88BDFc81ca69dcB1d924f59f0413A602a",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )


class OptimismContractSpecs:
    MultiSend = ContractSpec(
        address="0x187C0F98FEF80E87880Db50241D40551eDd027Bf",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )


class ArbitrumContractSpecs:
    MultiSend = ContractSpec(
        address="0x842ec2c7d803033edf55e478f461fc547bc54eb2", #multicall2 instead of multicall but fine
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )



ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
}

