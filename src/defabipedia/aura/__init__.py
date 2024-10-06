from ..types import Chain, ContractAbi, ContractSpec, current_dir


class AllAbis:
    BaseRewardPool = ContractAbi(abi_path=current_dir() / "base_reward_pool.json", name="base_reward_pool")


class EthereumContractSpecs:
    Booster = ContractSpec(
        address="0xA57b8d98dAE62B26Ec3bcC4a365338157060B234", abi_path=current_dir() / "booster.json", name="booster"
    )
    ClaimZap = ContractSpec(
        address="0x5b2364fD757E262253423373E4D57C5c011Ad7F4",
        abi_path=current_dir() / "eth_claim_zap.json",
        name="claim_zap",
    )


class GnosisContractSpecs:
    Booster = ContractSpec(
        address="0x98Ef32edd24e2c92525E59afc4475C1242a30184", abi_path=current_dir() / "booster.json", name="booster"
    )
    ClaimZap = ContractSpec(
        address="0x4EA38a5739D467F7f84c06155ee2Ad745E5328E8",
        abi_path=current_dir() / "gc_claim_zap.json",
        name="claim_zap",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}

Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
