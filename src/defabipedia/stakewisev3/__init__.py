from ..types import Chain, ContractAbi, ContractSpec, current_dir


class GnosisAbis:
    StakingVault = ContractAbi(abi_path=current_dir() / "stake_vault.json", name="stake_vault")


class EthereumAbis:
    OsVaultController = ContractAbi(
        abi_path=current_dir() / "os_token_vault_controller.json", name="os_token_vault_controller"
    )


class EthereumContractSpecs:
    OsVaultController = ContractSpec(
        address="0x2A261e60FB14586B474C208b1B7AC6D0f5000306",
        abi_path=current_dir() / "os_token_vault_controller.json",
        name="os_token_vault_controller",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}

Abis = {Chain.GNOSIS: GnosisAbis, Chain.ETHEREUM: EthereumAbis}
