from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    gas_replenisher = ContractAbi(abi_path=parent(__file__) / "gas_replenisher.json", name="gas_replenisher")


Abis = {
    Chain.ETHEREUM: AllAbis,
    Chain.BASE: AllAbis,
    Chain.ARBITRUM: AllAbis,
    Chain.OPTIMISM: AllAbis,
    Chain.GNOSIS: AllAbis,
}
