from ..types import Chain, ContractSpec, ContractAbi, current_dir


class AllAbis:
    ComposableStablePool = ContractAbi(abi_path=current_dir() / 'composable_stable_pool.json', name='composable_stable_pool')
    WeightedPool = ContractAbi(abi_path=current_dir() / 'weighted_pool.json', name='weighted_pool')
    MetaStablePool = ContractAbi(abi_path=current_dir() / 'meta_stable_pool.json', name='meta_stable_pool')
    StablePool = ContractAbi(abi_path=current_dir() / 'stable_pool.json', name='stable_pool')
    # The universal_bpt contains all the functions of all kinds of pools
    UniversalBPT = ContractAbi(abi_path=current_dir() / 'universal_bpt.json', name='universal_bpt')
    Gauge = ContractAbi(abi_path=current_dir() / 'gauge.json', name='gauge')


class EthereumContractSpecs:
    Vault = ContractSpec(address='0xBA12222222228d8Ba445958a75a0704d566BF2C8',
                         abi_path=current_dir() / 'vault.json',
                         name='vault')
    Queries = ContractSpec(address="0xE39B5e3B6D74016b2F6A9673D7d7493B6DF549d5",
                           abi_path=current_dir() / 'queries.json',
                           name='queries')


class GnosisContractSpecs:
    Vault = ContractSpec(address='0xBA12222222228d8Ba445958a75a0704d566BF2C8',
                         abi_path=current_dir() / 'vault.json',
                         name='vault')
    Queries = ContractSpec(address="0xE39B5e3B6D74016b2F6A9673D7d7493B6DF549d5",
                           abi_path=current_dir() / 'queries.json',
                           name='queries')


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs
}

Abis = {
    Chain.ETHEREUM: AllAbis,
    Chain.GNOSIS: AllAbis
}
