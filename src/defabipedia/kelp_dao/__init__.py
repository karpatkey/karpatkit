from ..types import Chain, ContractAbi, parent


class AllAbis:
    WithdrawalManager = ContractAbi(abi_path=parent(__file__) / "withdrawal_manager.json", name="withdrawal_manager")


Abis = {Chain.ETHEREUM: AllAbis}
