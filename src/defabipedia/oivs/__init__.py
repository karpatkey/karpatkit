from defabipedia.types import Chain, ContractAbi, parent


class AllAbis:
    nav_calculator = ContractAbi(abi_path=parent(__file__) / "nav_calculator.json", name="nav_calculator")


Abis = {
    Chain.ETHEREUM: AllAbis,
    Chain.GNOSIS: AllAbis,
    Chain.OPTIMISM: AllAbis,
    Chain.ARBITRUM: AllAbis,
    Chain.BASE: AllAbis,
}
