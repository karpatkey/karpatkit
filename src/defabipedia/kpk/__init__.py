from defabipedia.types import Chain, ContractAbi, parent


class AllAbis:
    kpkShares = ContractAbi(abi_path=parent(__file__) / "shares_v2.json", name="kpkShares")
    NAVCalculator = ContractAbi(abi_path=parent(__file__) / "nav_calculator.json", name="NAVCalculator")


Abis = {
    Chain.ETHEREUM: AllAbis,
    Chain.GNOSIS: AllAbis,
    Chain.OPTIMISM: AllAbis,
    Chain.ARBITRUM: AllAbis,
    Chain.BASE: AllAbis,
}
