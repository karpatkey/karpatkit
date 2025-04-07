from defabipedia.types import Chain, ContractAbi, ContractSpec, parent


class GnosisContractSpecs:
    LoanToken = ContractSpec(
        address="0x4440C069272cC34b80C7B11bEE657D0349Ba9C23",
        abi_path=parent(__file__) / "loan_token.json",
        name="LoanToken",
    )


class GnosisAbis:
    LoanContract = ContractAbi(
        abi_path=parent(__file__) / "loan_contract.json", name="LoanContract"
    )


ContractSpecs = {Chain.GNOSIS: GnosisContractSpecs}

Abis = {Chain.GNOSIS: GnosisAbis}
