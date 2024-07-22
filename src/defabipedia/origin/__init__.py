from defabipedia.types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    oETH = ContractSpec(
        address="0x856c4Efb76C1D1AE02e20CEB03A2A6a08b0b8dC3", abi_path=current_dir() / "oeth.json", name="oETH"
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
