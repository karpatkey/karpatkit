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
        address="0xF25212E676D1F7F89Cd72fFEe66158f541246445",
        abi_path=current_dir() / "polygon_cUSDCv3.json",
        name="cUSDCv3",
    )
    cUSDCv3_ext = ContractSpec(
        address="0xbdE8F31D2DdDA895264e27DD990faB3DC87b372d",
        abi_path=current_dir() / "polygon_cUSDCv3_ext.json",
        name="cUSDCv3_ext",
    )
    cUSDTv3 = ContractSpec(
        address="0xaeB318360f27748Acb200CE616E389A6C9409a07",
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
        abi_path=current_dir() / "polygon_proxy_admin.json",
        name="comet_proxy_admin",
    )
    rewards = ContractSpec(
        address="0x45939657d1CA34A8FA39A924B71D28Fe8431e581",
        abi_path=current_dir() / "polygon_rewards.json",
        name="rewards",
    )
    configurator = ContractSpec(
        address="0x83E0F742cAcBE66349E3701B171eE2487a26e738",
        abi_path=current_dir() / "polygon_configurator.json",
        name="configurator",
    )
    bridge_receiver = ContractSpec(
        address="0x18281dfC4d00905DA1aaA6731414EABa843c468A",
        abi_path=current_dir() / "polygon_bridge_receiver.json",
        name="bridge_receiver",
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
        address="0xc3d688B66703497DAA19211EEdff47f25384cdc3",
        abi_path=current_dir() / "eth_cUSDCv3.json",
        name="cUSDCv3",
    )
    cUSDCv3_ext = ContractSpec(
        address="0x285617313887d43256F852cAE0Ee4de4b68D45B0",
        abi_path=current_dir() / "eth_cUSDCv3_ext.json",
        name="cUSDCv3_ext",
    )
    cUSDTv3 = ContractSpec(
        address="0x3Afdc9BCA9213A35503b077a6072F3D0d5AB0840",
        abi_path=current_dir() / "eth_cUSDTv3.json",
        name="cUSDTv3",
    )
    cUSDTv3_ext = ContractSpec(
        address="0x5C58d4479A1E9b2d19EE052143FA73F0ee79A36e",
        abi_path=current_dir() / "eth_cUSDTv3_ext.json",
        name="cUSDTv3_ext",
    )
    cWETHv3 = ContractSpec(
        address="0xA17581A9E3356d9A858b789D68B4d866e593aE94",
        abi_path=current_dir() / "eth_cWETHv3.json",
        name="cWETHv3",
    )
    cWETHv3_ext = ContractSpec(
        address="0xe2C1F54aFF6b38fD9DF7a69F22cB5fd3ba09F030",
        abi_path=current_dir() / "eth_cWETHv3_ext.json",
        name="cWETHv3_ext",
    )
    cbETH = ContractSpec(
        address="0xBe9895146f7AF43049ca1c1AE358B0541Ea49704",
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
    cwstETHv3 = ContractSpec(
        address="0x3D0bb1ccaB520A66e607822fC55BC921738fAFE3",
        abi_path=current_dir() / "eth_cwstETHv3.json",
        name="cwstETHv3",
    )
    cwstETHv3_ext = ContractSpec(
        address="0x995E394b8B2437aC8Ce61Ee0bC610D617962B214",
        abi_path=current_dir() / "eth_cwstETHv3_ext.json",
        name="cwstETHv3_ext",
    )
    governor = ContractSpec(
        address="0xc0Da02939E1441F497fd74F78cE7Decb17B66529",
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
        address="0x316f9708bB98af7dA9c68C1C3b5e79039cD336E3",
        abi_path=current_dir() / "eth_configurator.json",
        name="configurator",
    )
    timelock = ContractSpec(
        address="0x6d903f6003cca6255D85CcA4D3B5E5146dC33925",
        abi_path=current_dir() / "eth_timelock.json",
        name="timelock",
    )
class OptimismContractSpecs:
    base_bulker = ContractSpec(
        address="0xcb3643CC8294B23171272845473dEc49739d4Ba3",
        abi_path=current_dir() / "optimism_base_bulker.json",
        name="base_bulker",
    )
    bridge_receiver = ContractSpec(
        address="0xC3a73A70d1577CD5B02da0bA91C0Afc8fA434DAF",
        abi_path=current_dir() / "optimism_bridge_receiver.json",
        name="bridge_receiver",
    )
    cUSDCv3 = ContractSpec(
        address="0x2e44e174f7D53F0212823acC11C01A11d58c5bCB",
        abi_path=current_dir() / "optimism_cUSDCv3.json",
        name="cUSDCv3",
    )
    cUSDCv3_ext = ContractSpec(
        address="0xE802a0b833f6080FEB46DD54c75444c5dba0c873",
        abi_path=current_dir() / "optimism_cUSDCv3_ext.json",
        name="cUSDCv3_ext",
    )
    cUSDTv3 = ContractSpec(
        address="0x995E394b8B2437aC8Ce61Ee0bC610D617962B214",
        abi_path=current_dir() / "optimism_cUSDTv3.json",
        name="cUSDTv3",
    )
    cUSDTv3_ext = ContractSpec(
        address="0xC49399814452B41dA8a7cd76a159f5515cb3e493",
        abi_path=current_dir() / "optimism_cUSDTv3_ext.json",
        name="cUSDTv3_ext",
    )
    cWETHv3 = ContractSpec(
        address="0xE36A30D249f7761327fd973001A32010b521b6Fd",
        abi_path=current_dir() / "optimism_cWETHv3.json",
        name="cUSDTv3",
    )
    cWETHv3_ext = ContractSpec(
        address="0x82B8d9A06ccABC1e9B0c0A00f38B858E6925CF2f",
        abi_path=current_dir() / "optimism_cWETHv3_ext.json",
        name="cUSDTv3_ext",
    )
    comet_factory = ContractSpec(
        address="0xFa454dE61b317b6535A0C462267208E8FdB89f45",
        abi_path=current_dir() / "optimism_comet_factory.json",
        name="comet_factory",
    )
    configurator = ContractSpec(
        address="0x84E93EC6170ED630f5ebD89A1AAE72d4F63f2713",
        abi_path=current_dir() / "optimism_configurator.json",
        name="configurator",
    )
    comet_proxy_admin = ContractSpec(
        address="0x3C30B5a5A04656565686f800481580Ac4E7ed178",
        abi_path=current_dir() / "optimism_proxy_admin.json",
        name="comet_proxy_admin",
    )
    rewards = ContractSpec(
        address="0x443EA0340cb75a160F31A440722dec7b5bc3C2E9",
        abi_path=current_dir() / "optimism_rewards.json",
        name="rewards",
    )
    timelock = ContractSpec(
        address="0xd98Be00b5D27fc98112BdE293e487f8D4cA57d07",
        abi_path=current_dir() / "optimism_timelock.json",
        name="timelock",
    )

class GnosisContractSpecs:
    pass


class ArbitrumContractSpecs:
    pass

#test

ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
    Chain.POLYGON: PolygonContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
}
