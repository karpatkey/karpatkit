from defabipedia.types import Chain, ContractAbi, ContractSpec, parent


class EthereumContractSpecs:
    market_factory = ContractSpec(
        address="0x1A6fCc85557BC4fB7B534ed835a03EF056552D52",
        abi_path=parent(__file__) / "market_factory_v3.json",
        name="market_factory_v3",
    )


class EthereumAbis:
    PendleMarketV3 = ContractAbi(abi_path=parent(__file__) / "pendle_market_v3.json", name="PendleMarketV3")
    PrincipalToken = ContractAbi(
        abi_path=parent(__file__) / "principal_token.json",
        name="PrincipalToken",
    )
    StandardizedToken = ContractAbi(abi_path=parent(__file__) / "standardized_token.json", name="StandardizedToken")


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}

Abis = {Chain.ETHEREUM: EthereumAbis}
