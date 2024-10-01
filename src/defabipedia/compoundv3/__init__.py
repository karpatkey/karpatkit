from ..types import Chain, ContractAbi, ContractSpec, current_dir


class AllAbis:
    Comet = ContractAbi(abi_path=current_dir() / "comet_factory.json", name="comet_factory")
    Rewards = ContractAbi(abi_path=current_dir() / "eth_rewards.json", name="rewards")


Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}


class PolygonContractSpecs:
    base_bulker = ContractSpec(
        address="0x59e242D352ae13166B4987aE5c990C232f7f7CD6",
        abi_path=current_dir() / "polygon_base_bulker.json",
        name="base_bulker",
    )
    cUSDCv3 = ContractSpec(
        address="0xc70e3ed4b719e4d62c780507e1f1340ff8b9bed2",
        abi_path=current_dir() / "polygon_cUSDCv3.json",
        name="cUSDCv3",
    )
    cUSDCv3_ext = ContractSpec(
        address="0xbdE8F31D2DdDA895264e27DD990faB3DC87b372d",
        abi_path=current_dir() / "polygon_cUSDCv3_ext.json",
        name="cUSDCv3_ext",
    )
    cUSDTv3 = ContractSpec(
        address="0xAe2cCD85e75f885449561a1A8BF6605b38662093",
        abi_path=current_dir() / "polygon_cUSDTv3.json",
        name="cUSDTv3",
    )
    cUSDTv3_ext = ContractSpec(
        address="0x2F4eAF29dfeeF4654bD091F7112926E108eF4Ed0",
        abi_path=current_dir() / "polygon_cUSDTv3_ext.json",
        name="cUSDTv3_ext",
    )
    comet_factory = ContractSpec(
        address="0x2F9E3953b2Ef89fA265f2a32ed9F80D00229125B",
        abi_path=current_dir() / "polygon_comet_factory.json",
        name="comet_factory",
    )
    comet_proxy_admin = ContractSpec(
        address="0xd712ACe4ca490D4F3E92992Ecf3DE12251b975F9",
        abi_path=current_dir() / "polygon_comet_proxy_admin.json",
        name="comet_proxy_admin",
    )
    comet_rewards = ContractSpec(
        address="0x45939657d1CA34A8FA39A924B71D28Fe8431e581",
        abi_path=current_dir() / "polygon_comet_rewards.json",
        name="comet_rewards",
    )
    configurator = ContractSpec(
        address="0x9c4ec768c28520B50860ea7a15bd7213a9fF58bf",
        abi_path=current_dir() / "polygon_configurator.json",
        name="configurator",
    )
    polygon_bridge_receiver = ContractSpec(
        address="0x18281dfC4d00905DA1aaA6731414EABa843c468A",
        abi_path=current_dir() / "polygon_bridge_receiver.json",
        name="polygon_bridge_receiver",
    )
    timelock = ContractSpec(
        address="0xCC3E7c85Bb0EE4f09380e041fee95a0caeDD4a02",
        abi_path=current_dir() / "polygon_timelock.json",
        name="timelock",
    )


class EthereumContractSpecs:
    base_bulker_USDC = ContractSpec(
        address="0x74a81F84268744a40FEBc48f8b812a1f188D80C3",
        abi_path=current_dir() / "eth_base_bulker_USDC.json",
        name="base_bulker_USDC",
    )
    base_bulker = ContractSpec(
        address="0xa397a8C2086C554B531c02E29f3291c9704B00c7",
        abi_path=current_dir() / "eth_base_bulker.json",
        name="base_bulker",
    )
    cUSDCv3 = ContractSpec(
        address="0xAFb1Df7261B52Ba6273a3aD0ED7eD7B6b22Ff6Ef",
        abi_path=current_dir() / "eth_cUSDCv3.json",
        name="cUSDCv3",
    )
    cUSDCv3_ext = ContractSpec(
        address="0x285617313887d43256F852cAE0Ee4de4b68D45B0",
        abi_path=current_dir() / "eth_cUSDCv3_ext.json",
        name="cUSDCv3_ext",
    )
    cUSDTv3 = ContractSpec(
        address="0xbeaf5b4e12a380f6e211181de6bfecd18bb99a8f",
        abi_path=current_dir() / "eth_cUSDTv3.json",
        name="cUSDTv3",
    )
    cUSDTv3_ext = ContractSpec(
        address="0x5C58d4479A1E9b2d19EE052143FA73F0ee79A36e",
        abi_path=current_dir() / "eth_cUSDTv3_ext.json",
        name="cUSDTv3_ext",
    )
    cWETHv3 = ContractSpec(
        address="0x8b1fe29326dc8b02e79566e84431a5cbc3c7c7dc",
        abi_path=current_dir() / "eth_cWETHv3.json",
        name="cWETHv3",
    )
    cWETHv3_ext = ContractSpec(
        address="0xe2C1F54aFF6b38fD9DF7a69F22cB5fd3ba09F030",
        abi_path=current_dir() / "eth_cWETHv3_ext.json",
        name="cWETHv3_ext",
    )
    cbETH = ContractSpec(
        address="0x31724cA0C982A31fbb5C57f4217AB585271fc9a5",
        abi_path=current_dir() / "eth_cbETH.json",
        name="cbETH",
    )
    comet_factory_USDT_wstETH = ContractSpec(
        address="0x698A949f3b4f7a5DdE236106F25Fa0eAcA0FcEF1",
        abi_path=current_dir() / "eth_comet_factory_USDT_wstETH.json",
        name="comet_factory_USDT_wstETH",
    )
    comet_factory_WETH_USDC = ContractSpec(
        address="0xa7F7De6cCad4D83d81676717053883337aC2c1b4",
        abi_path=current_dir() / "eth_comet_factory_WETH_USDC.json",
        name="comet_factory_WETH_USDC",
    )
    configurator_implementation = ContractSpec(
        address="0xcFC1fA6b7ca982176529899D99af6473aD80DF4F",
        abi_path=current_dir() / "eth_configurator_implementation.json",
        name="configurator_implementation",
    )
    cwstETHv3 = ContractSpec(
        address="0x1f0aa640e4871793ac10029365febe4e8e4b1441",
        abi_path=current_dir() / "eth_cwstETHv3.json",
        name="cwstETHv3",
    )
    cwstETHv3_ext = ContractSpec(
        address="0x995E394b8B2437aC8Ce61Ee0bC610D617962B214",
        abi_path=current_dir() / "eth_cwstETHv3_ext.json",
        name="cwstETHv3_ext",
    )
    governor = ContractSpec(
        address="0x6F6e4785c97885d26466945055d4Ae8931bE6f7a",
        abi_path=current_dir() / "eth_governor.json",
        name="governor",
    )
    proxy_admin = ContractSpec(
        address="0x1EC63B5883C3481134FD50D5DAebc83Ecd2E8779",
        abi_path=current_dir() / "eth_proxy_admin.json",
        name="proxy_admin",
    )
    rewards = ContractSpec(
        address="0x1B0e765F6224C21223AeA2af16c1C46E38885a40",
        abi_path=current_dir() / "eth_rewards.json",
        name="rewards",
    )
    configurator = ContractSpec(
        address="0x9c4ec768c28520B50860ea7a15bd7213a9fF58bf",
        abi_path=current_dir() / "polygon_configurator.json",
        name="configurator",
    )
    timelock = ContractSpec(
        address="0x6d903f6003cca6255D85CcA4D3B5E5146dC33925",
        abi_path=current_dir() / "eth_timelock.json",
        name="timelock",
    )


class GnosisContractSpecs:
    pass


class ArbitrumContractSpecs:
    pass


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
    Chain.POLYGON: PolygonContractSpecs,
}
