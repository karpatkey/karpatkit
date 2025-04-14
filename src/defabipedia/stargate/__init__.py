from ..types import Chain, ContractAbi, parent


class GnosisAbis:
    StakingVault = ContractAbi(abi_path=parent(__file__) / "pool.json", name="pool")


Abis = {Chain.GNOSIS: GnosisAbis}
