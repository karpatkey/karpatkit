from defabipedia.types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall3.json",
        name="multicall3",
    )


class GnosisContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall3.json",
        name="multicall3",
    )


class OptimismContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall3.json",
        name="multicall3",
    )


class ArbitrumContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11", #multicall2 instead of multicall but fine
        abi_path=parent(__file__) / "multicall3.json",
        name="multical3",
    )



ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
}

