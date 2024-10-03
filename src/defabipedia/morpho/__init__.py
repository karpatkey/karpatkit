from ..types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    morpho_blue = ContractSpec(
        address="0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb",
        abi_path=current_dir() / "morpho_blue.json",
        name="morpho_blue",
    )


class BaseContractSpecs:
    morpho_blue = ContractSpec(
        address="0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb",
        abi_path=current_dir() / "base_morpho_blue.json",
        name="morpho_blue",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.BASE: BaseContractSpecs}
