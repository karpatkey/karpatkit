from ..types import Chain, ContractAbi, ContractSpec, parent


class GnosisAbis:
    StakingVault = ContractAbi(abi_path=parent(__file__) / "stake_vault.json", name="stake_vault")


class EthereumAbis:
    OsVaultController = ContractAbi(
        abi_path=parent(__file__) / "os_token_vault_controller.json", name="os_token_vault_controller"
    )


class EthereumContractSpecs:
    OsVaultController = ContractSpec(
        address="0x2A261e60FB14586B474C208b1B7AC6D0f5000306",
        abi_path=parent(__file__) / "os_token_vault_controller.json",
        name="os_token_vault_controller",
    )


class GnosisContractSpecs:
    OsVaultController = ContractSpec(
        address="0x60B2053d7f2a0bBa70fe6CDd88FB47b579B9179a",
        abi_path=parent(__file__) / "os_token_vault_controller.json",
        name="os_token_vault_controller",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}

Abis = {Chain.GNOSIS: GnosisAbis, Chain.ETHEREUM: EthereumAbis}
