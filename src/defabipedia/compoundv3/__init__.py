from ..types import Chain, ContractAbi, current_dir

class AllAbis:
    Comet = ContractAbi(abi_path=current_dir() / "comet_factory.json", name="comet_factory")
    CometRewards = ContractAbi(abi_path=current_dir() / "comet_rewards.json", name="comet_rewards")

Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}

class PolygonContractSpecs:
    base_bulker = ContractSpec(
        address="0x59e242D352ae13166B4987aE5c990C232f7f7CD6",
        abi_path=current_dir() / "base_bulker.json",
        name="base_bulker",
    )
    cUSDCv3 = ContractSpec(
        address="0xc70e3ed4b719e4d62c780507e1f1340ff8b9bed2",
        abi_path=current_dir() / "cUSDCv3.json",
        name="cUSDCv3",
    )
    cUSDCv3_ext = ContractSpec(
        address="0xbdE8F31D2DdDA895264e27DD990faB3DC87b372d",
        abi_path=current_dir() / "cUSDCv3_ext.json",
        name="cUSDCv3_ext",
    )
    cUSDTv3 = ContractSpec(
        address="0xAe2cCD85e75f885449561a1A8BF6605b38662093",
        abi_path=current_dir() / "cUSDTv3.json",
        name="cUSDTv3",
    )
    cUSDTv3_ext = ContractSpec(
        address="0x2F4eAF29dfeeF4654bD091F7112926E108eF4Ed0",
        abi_path=current_dir() / "cUSDTv3_ext.json",
        name="cUSDTv3_ext",
    )
    comet_factory = ContractSpec(
        address="0x2F9E3953b2Ef89fA265f2a32ed9F80D00229125B",
        abi_path=current_dir() / "comet_factory.json",
        name="comet_factory",
    )
    comet_proxy_admin = ContractSpec(
        address="0xd712ACe4ca490D4F3E92992Ecf3DE12251b975F9",
        abi_path=current_dir() / "comet_proxy_admin.json",
        name="comet_proxy_admin",
    )
    comet_rewards = ContractSpec(
        address="0x45939657d1CA34A8FA39A924B71D28Fe8431e581",
        abi_path=current_dir() / "comet_rewards.json",
        name="comet_rewards",
    )
    configurator = ContractSpec(
        address="0x9c4ec768c28520B50860ea7a15bd7213a9fF58bf",
        abi_path=current_dir() / "configurator.json",
        name="configurator",
    )
    polygon_bridge_receiver = ContractSpec(
        address="0x18281dfC4d00905DA1aaA6731414EABa843c468A",
        abi_path=current_dir() / "polygon_bridge_receiver.json",
        name="polygon_bridge_receiver",
    )
    timelock = ContractSpec(
        address="0xCC3E7c85Bb0EE4f09380e041fee95a0caeDD4a02",
        abi_path=current_dir() / "timelock.json",
        name="timelock",
    )
    
ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs, Chain.ARBITRUM: ArbitrumContractSpecs, Chain.POLYGON: ArbitrumContractSpecs}
