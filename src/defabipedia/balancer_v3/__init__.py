from ..types import Chain, ContractAbi, parent


class AllAbis:
    liquidity_pool = ContractAbi(abi_path=parent(__file__) / "liquidity_pool.json", name="liquidity_pool.json")


Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
