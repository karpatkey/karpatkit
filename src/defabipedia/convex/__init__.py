from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    BaseRewardPool = ContractAbi(abi_path=parent(__file__) / "base_reward_pool.json", name="base_reward_pool")


class EthereumContractSpecs:
    ClaimZap = ContractSpec(
        address="0x3f29cB4111CbdA8081642DA1f75B3c12DECf2516",
        abi_path=parent(__file__) / "claim_zap.json",
        name="claim_zap",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
}

Abis = {Chain.ETHEREUM: AllAbis}
