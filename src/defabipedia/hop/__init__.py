from ..types import Chain, ContractAbi, ContractSpec, current_dir


class AllAbis:
    LiquidityPool = ContractAbi(
        abi_path=current_dir() / "liquidity_pool.json", name="liquidity_pool"
    )
    LiquidityPoolToken = ContractAbi(
        abi_path=current_dir() / "liquidity_pool_token.json", name="liquidity_pool_token"
    )
    Rewarder = ContractAbi(abi_path=current_dir() / "rewarder.json", name="rewarder")


Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
