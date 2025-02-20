from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    ComposableStablePool = ContractAbi(
        abi_path=parent(__file__) / "composable_stable_pool.json", name="composable_stable_pool"
    )
    WeightedPool = ContractAbi(abi_path=parent(__file__) / "weighted_pool.json", name="weighted_pool")
    MetaStablePool = ContractAbi(abi_path=parent(__file__) / "meta_stable_pool.json", name="meta_stable_pool")
    StablePool = ContractAbi(abi_path=parent(__file__) / "stable_pool.json", name="stable_pool")
    # The universal_bpt contains all the functions of all kinds of pools
    UniversalBPT = ContractAbi(abi_path=parent(__file__) / "universal_bpt.json", name="universal_bpt")
    Gauge = ContractAbi(abi_path=parent(__file__) / "gauge.json", name="gauge")


class EthereumContractSpecs:
    Vault = ContractSpec(
        address="0xBA12222222228d8Ba445958a75a0704d566BF2C8", abi_path=parent(__file__) / "vault.json", name="vault"
    )
    Queries = ContractSpec(
        address="0xE39B5e3B6D74016b2F6A9673D7d7493B6DF549d5", abi_path=parent(__file__) / "queries.json", name="queries"
    )
    LiquidityGaugeFactory = ContractSpec(
        address="0x4E7bBd911cf1EFa442BC1b2e9Ea01ffE785412EC",
        abi_path=parent(__file__) / "gauge_factory.json",
        name="gauge_factory",
    )
    LiquidityGaugeFactory2 = ContractSpec(
        address="0xf1665e19bc105be4edd3739f88315cc699cc5b65",
        abi_path=parent(__file__) / "gauge_factory2.json",
        name="gauge_factory2",
    )

    BCowFactory = ContractSpec(
        address="0xf76c421bAb7df8548604E60deCCcE50477C10462",
        abi_path=parent(__file__) / "bcow_factory.json",
        name="bcow_factory",
    )


class GnosisContractSpecs:
    Vault = ContractSpec(
        address="0xBA12222222228d8Ba445958a75a0704d566BF2C8", abi_path=parent(__file__) / "vault.json", name="vault"
    )
    Queries = ContractSpec(
        address="0x0F3e0c4218b7b0108a3643cFe9D3ec0d4F57c54e", abi_path=parent(__file__) / "queries.json", name="queries"
    )
    LiquidityGaugeFactory = ContractSpec(
        address="0x809B79b53F18E9bc08A961ED4678B901aC93213a",
        abi_path=parent(__file__) / "gauge_factory.json",
        name="gauge_factory",
    )
    LiquidityGaugeFactory2 = ContractSpec(
        address="0x83E443EF4f9963C77bd860f94500075556668cb8",
        abi_path=parent(__file__) / "gauge_factory2.json",
        name="gauge_factory2",
    )

    BCowFactory = ContractSpec(
        address="0x703Bd8115E6F21a37BB5Df97f78614ca72Ad7624",
        abi_path=parent(__file__) / "bcow_factory.json",
        name="bcow_factory",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}

Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
