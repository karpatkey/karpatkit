from defabipedia.types import Chain, ContractAbi, parent


class AllAbis:
    Collector = ContractAbi(abi_path=parent(__file__) / "collector.json", name="Collector")


Abis = {
    Chain.ETHEREUM: AllAbis,
}
