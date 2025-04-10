from ..types import Chain, ContractAbi, ContractSpec, parent


class EthereumAbis:
    FundValueCalculator = ContractAbi(
        abi_path=parent(__file__) / "fund_value_calculator.json", name="fund_value_calculator"
    )

    DivaStethVault = ContractAbi(abi_path=parent(__file__) / "diva_steth_vault.json", name="diva_steth_vault")


class EthereumContractSpecs:
    FundValueCalculator = ContractSpec(
        address="0x7c728cd0CfA92401E01A4849a01b57EE53F5b2b9",
        abi_path=parent(__file__) / "fund_value_calculator.json",
        name="fund_value_calculator",
    )

    DivaStethVault = ContractSpec(
        address="0xA1F2d3E6b5C8F7aB4fA9c8C9D9eD4E5fB8c4f5C0",
        abi_path=parent(__file__) / "diva_steth_vault.json",
        name="diva_steth_vault",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}

Abis = {Chain.ETHEREUM: EthereumAbis}
