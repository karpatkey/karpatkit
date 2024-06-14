from ..types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    CowswapSigner = ContractSpec(
        address="0x78E9e622A57f70F1E0Ec652A4931E4e278e58142",
        abi_path=current_dir() / "pool_manager.json",
        name="pool_manager",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
