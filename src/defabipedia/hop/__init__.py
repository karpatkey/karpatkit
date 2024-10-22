from ..types import Chain, ContractAbi, parent


class AllAbis:
    LiquidityPool = ContractAbi(abi_path=parent(__file__) / "liquidity_pool.json", name="liquidity_pool")
    LiquidityPoolToken = ContractAbi(
        abi_path=parent(__file__) / "liquidity_pool_token.json", name="liquidity_pool_token"
    )
    Rewarder = ContractAbi(abi_path=parent(__file__) / "rewarder.json", name="rewarder")


Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
