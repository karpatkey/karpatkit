from defabipedia.types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    oETH = ContractSpec(
        address="0xEc5d0801fCDaf14E6F72a0FD877581e5b7617c87", abi_path=current_dir() / "oeth.json", name="oETH"
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
