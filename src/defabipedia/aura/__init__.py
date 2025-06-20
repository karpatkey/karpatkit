from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    BaseRewardPool = ContractAbi(
        abi_path=parent(__file__) / "base_reward_pool.json", name="base_reward_pool"
    )


class EthereumContractSpecs:
    Booster = ContractSpec(
        address="0xA57b8d98dAE62B26Ec3bcC4a365338157060B234",
        abi_path=parent(__file__) / "booster.json",
        name="booster",
    )
    ClaimZap = ContractSpec(
        address="0x5b2364fD757E262253423373E4D57C5c011Ad7F4",
        abi_path=parent(__file__) / "eth_claim_zap.json",
        name="claim_zap",
    )
    vlAura = ContractSpec(
        address="0x3Fa73f1E5d8A792C80F426fc8F84FBF7Ce9bBCAC",
        abi_path=parent(__file__) / "vl_aura.json",
        name="vl_aura",
    )
    auraBalCompoundingRewards = ContractSpec(
        address="0xAc16927429c5c7Af63dD75BC9d8a58c63FfD0147",
        abi_path=parent(__file__) / "aurabal_compounding_rewards.json",
        name="aurabal_compounding_rewards",
    )


class GnosisContractSpecs:
    Booster = ContractSpec(
        address="0x98Ef32edd24e2c92525E59afc4475C1242a30184",
        abi_path=parent(__file__) / "booster.json",
        name="booster",
    )
    ClaimZap = ContractSpec(
        address="0x4EA38a5739D467F7f84c06155ee2Ad745E5328E8",
        abi_path=parent(__file__) / "gc_claim_zap.json",
        name="claim_zap",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
}

Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
