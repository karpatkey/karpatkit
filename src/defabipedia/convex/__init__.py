from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    BaseRewardPool = ContractAbi(abi_path=parent(__file__) / "base_reward_pool.json", name="base_reward_pool")


class EthereumContractSpecs:
    Booster = ContractSpec(
        address="0xF403C135812408BFbE8713b5A23a04b3D48AAE31",
        abi_path=parent(__file__) / "booster.json",
        name="booster",
    )
    ClaimZap = ContractSpec(
        address="0x3f29cB4111CbdA8081642DA1f75B3c12DECf2516",
        abi_path=parent(__file__) / "claim_zap.json",
        name="claim_zap",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
}

Abis = {Chain.ETHEREUM: AllAbis}
