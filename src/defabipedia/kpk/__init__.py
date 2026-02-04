from ..types import Chain, ContractAbi, parent


class AllAbis:
    AaveLeveragedPosition = ContractAbi(
        abi_path=parent(__file__) / "aave_leveraged_position.json",
        name="AaveLeveragedPosition",
    )


Abis = {Chain.ETHEREUM: AllAbis}
