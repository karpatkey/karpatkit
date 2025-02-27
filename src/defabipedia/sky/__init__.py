from defabipedia.types import Chain, ContractSpec, parent

class EthereumContractSpecs:
    sUSDS = ContractSpec(
        address="0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD",
        abi_path=parent(__file__) / "susds.json",
        name="sUSDS",
    )

ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}