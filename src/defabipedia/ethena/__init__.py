from ..types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    sUSDe = ContractSpec(
        address="0x9D39A5DE30e57443BfF2A8307A4256c8797A3497",
        abi_path=parent(__file__) / "sUSDe.json",
        name="sUSDe",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
