from ..types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    PoolManager = ContractSpec(
        address="0x78E9e622A57f70F1E0Ec652A4931E4e278e58142",
        abi_path=parent(__file__) / "pool_manager.json",
        name="pool_manager",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
