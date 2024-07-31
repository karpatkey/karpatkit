from ..types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    weETH = ContractSpec(
        address="0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee",
        abi_path=current_dir() / "weETH.json",
        name="weETH",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
