from ..types import Chain, ContractAbi, ContractSpec, current_dir


class AllAbis:
    Comet = ContractAbi(abi_path=current_dir() / "comet.json", name="comet")
    CometRewards = ContractAbi(abi_path=current_dir() / "comet_rewards.json", name="comet_rewards")


Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
