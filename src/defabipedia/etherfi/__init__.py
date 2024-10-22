from ..types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    weETH = ContractSpec(
        address="0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee",
        abi_path=parent(__file__) / "weETH.json",
        name="weETH",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
