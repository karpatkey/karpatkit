from ..types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    PoolManager = ContractSpec(
        address="0x91808B5E2F6d7483D41A681034D7c9DbB64B9E29",
        abi_path=parent(__file__) / "pool_manager.json",
        name="pool_manager",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
