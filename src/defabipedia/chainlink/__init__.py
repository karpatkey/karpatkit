from ..types import Chain, ContractAbi, ContractSpec, current_dir


class AllAbis:
    LiquidityPool = ContractAbi(
        abi_path=current_dir() / "liquidity_pool.json", name="liquidity_pool"
    )
    LiquidityPoolToken = ContractAbi(
        abi_path=current_dir() / "liquidity_pool_token.json", name="liquidity_pool_token"
    )
    Rewarder = ContractAbi(abi_path=current_dir() / "rewarder.json", name="rewarder")


class EthereumContractSpecs:
    GbpPriceFeed = ContractSpec(
        address="0x5c0Ab2d9b5a7ed9f470386e82BB36A3613cDd4b5", abi_path=current_dir() / "price_feed.json",
        name="price_feed"
    )


class GnosisContractSpecs:
    EurPriceFeed = ContractSpec(
        address="0xab70BCB260073d036d1660201e9d5405F5829b7a", abi_path=current_dir() / "price_feed.json",
        name="eur_price_feed"
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}

Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
