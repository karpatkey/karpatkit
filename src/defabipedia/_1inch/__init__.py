from defabipedia.types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    AggregationRouterV5 = ContractSpec(
        address="0x1111111254EEB25477B68fb85Ed929f73A960582",
        abi_path=parent(__file__) / "aggregation_router_v5.json",
        name="AggregationRouterV5",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
