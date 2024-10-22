from defabipedia.types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    oETH = ContractSpec(
        address="0x856c4Efb76C1D1AE02e20CEB03A2A6a08b0b8dC3", abi_path=parent(__file__) / "oeth.json", name="oETH"
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
