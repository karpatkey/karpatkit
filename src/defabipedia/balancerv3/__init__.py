from ..types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    sUSDe = ContractSpec(
        address="",
        abi_path=parent(__file__) / "liquidity_pool.json",
        name="liquidity_pool",
    )


class GnosisContractSpecs:
    Gnosis = ContractSpec(
        address="",
        abi_path=parent(__file__) / "liquidity_pool.json",
        name="liquidity_pool",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}
