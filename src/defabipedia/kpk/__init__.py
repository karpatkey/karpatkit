from ..types import Chain, ContractAbi, parent


class AllAbis:
    UnwindLeveragedPosition = ContractAbi(
        abi_path=parent(__file__) / "unwind_leveraged_position.json", name="unwind_leveraged_position"
    )
    DepositLeveragedPosition = ContractAbi(
        abi_path=parent(__file__) / "deposit_leveraged_position.json", name="deposit_leveraged_position"
    )


Abis = {Chain.ETHEREUM: AllAbis}
