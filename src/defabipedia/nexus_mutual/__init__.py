from defabipedia.types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    oETH = ContractSpec(
        address="0xcafeab03F219b7a8BCb92a5d61508A0AE16302b6",
        abi_path=parent(__file__) / "nexus_viewer.json",
        name="nexus_viewer",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
