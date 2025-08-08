from defabipedia.types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    PriceOracle = ContractAbi(abi_path=parent(__file__) / "price_oracle.json", name="price_oracle")
    aToken = ContractAbi(abi_path=parent(__file__) / "atoken.json", name="aToken")


class EthereumContractSpecs:
    UIPoolDataProvider = ContractSpec(
        address="0x3F78BBD206e4D3c504Eb854232EdA7e47E9Fd8FC",
        abi_path=parent(__file__) / "ui_pool_data_provider.json",
        name="UIPoolDataProvider",
    )

    ProtocolDataProvider = ContractSpec(
        address="0x7B4EB56E7CD4b454BA8ff71E4518426369a138a3",
        abi_path=parent(__file__) / "protocol_data_provider.json",
        name="ProtocolDataProvider",
    )
    PoolAddressesProvider = ContractSpec(
        address="0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e",
        abi_path=parent(__file__) / "protocol_address_provider.json",
        name="PoolAddressesProvider",
    )
    LendingPoolV3 = ContractSpec(
        address="0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2",
        abi_path=parent(__file__) / "lending_pool_v3.json",
        name="LendingPoolV3",
    )
    aWrappedNative = ContractSpec(
        address="0x4d5F47FA6A74757f35C14fD3a6Ef8E3C9BC514E8",
        abi_path=parent(__file__) / "aWrappedNative.json",
        name="aEthWeth",
    )
    aUSDC = ContractSpec(
        address="0x98C23E9d8f34FEFb1B7BD6a91B7FF122F4e16F5c", abi_path=parent(__file__) / "atoken.json", name="aUSDC"
    )
    aDAI = ContractSpec(
        address="0x018008bfb33d285247A21d44E50697654f754e63", abi_path=parent(__file__) / "atoken.json", name="aDAI"
    )
    asDAI = ContractSpec(
        address="0x4C612E3B15b96Ff9A6faED838F8d07d479a8dD4c", abi_path=parent(__file__) / "atoken.json", name="asDAI"
    )
    WrappedTokenGatewayV3 = ContractSpec(
        address="0x893411580e590D62dDBca8a703d61Cc4A8c7b2b9",
        abi_path=parent(__file__) / "wrapped_token_gateway_v3.json",
        name="WrappedTokenGatewayV3",
    )
    AAVE = ContractSpec(
        address="0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9", abi_path=parent(__file__) / "AAVE.json", name="Aave"
    )
    ABPT = ContractSpec(
        address="0x41A08648C3766F9F9d85598fF102a08f4ef84F84", abi_path=parent(__file__) / "ABPT.json", name="ABPT"
    )
    stkAAVE = ContractSpec(
        address="0x4da27a545c0c5b758a6ba100e3a049001de870f5", abi_path=parent(__file__) / "stkAAVE.json", name="stkAAVE"
    )
    stkABPT = ContractSpec(
        address="0xa1116930326D21fB917d5A27F1E9943A9595fb47", abi_path=parent(__file__) / "stkABPT.json", name="stkABPT"
    )
    variableDebtNATIVE = ContractSpec(
        address="0xeA51d7853EEFb32b6ee06b1C12E6dcCA88Be0fFE",
        abi_path=parent(__file__) / "variableDebtNative.json",
        name="variableDebtEthWeth",
    )
    stableDebtNATIVE = ContractSpec(
        address="0x102633152313C81cD80419b6EcF66d14Ad68949A",
        abi_path=parent(__file__) / "stableDebtNative.json",
        name="stableDebtEthWeth",
    )
    variableDebtUSDC = ContractSpec(
        address="0x72E95b8931767C79bA4EeE721354d6E99a61D004",
        abi_path=parent(__file__) / "variableDebt.json",
        name="variableDebtUSDC",
    )
    variableDebtDAI = ContractSpec(
        address="0xcF8d0c70c850859266f5C338b38F9D663181C314",
        abi_path=parent(__file__) / "variableDebt.json",
        name="variableDebtDAI",
    )
    ParaSwapRepayAdapter = ContractSpec(
        address="0x1809f186D680f239420B56948C58F8DbbCdf1E18",
        abi_path=parent(__file__) / "paraswap_repay_adapter.json",
        name="ParaSwapRepayAdapter",
    )
    ParaSwapLiquidityAdapter = ContractSpec(
        address="0x872fBcb1B582e8Cd0D0DD4327fBFa0B4C2730995",
        abi_path=parent(__file__) / "paraswap_liquidity_adapter.json",
        name="ParaSwapLiquidityAdapter",
    )
    GovernanceV2 = ContractSpec(
        address="0xEC568fffba86c094cf06b22134B23074DFE2252c",
        abi_path=parent(__file__) / "governance_v2.json",
        name="GovernanceV2",
    )
    GHO = ContractSpec(
        address="0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f", abi_path=parent(__file__) / "GHO.json", name="GHO"
    )

    AAVE_oracle = ContractSpec(
        address="0x54586bE62E3c3580375aE3723C145253060Ca0C2",
        abi_path=parent(__file__) / "AAVE_oracle.json",
        name="AaveOracle",
    )


class GnosisContractSpecs:
    ProtocolDataProvider = ContractSpec(
        address="0x501B4c19dd9C2e06E94dA7b6D5Ed4ddA013EC741",
        abi_path=parent(__file__) / "protocol_data_provider.json",
        name="ProtocolDataProvider",
    )
    PoolAddressesProvider = ContractSpec(
        address="0x36616cf17557639614c1cdDb356b1B83fc0B2132",
        abi_path=parent(__file__) / "protocol_address_provider.json",
        name="PoolAddressesProvider",
    )
    LendingPoolV3 = ContractSpec(
        address="0xb50201558B00496A145fE76f7424749556E326D8",
        abi_path=parent(__file__) / "lending_pool_v3.json",
        name="LendingPoolV3",
    )
    WrappedTokenGatewayV3 = ContractSpec(
        address="0xfE76366A986B72c3f2923e05E6ba07b7de5401e4",
        abi_path=parent(__file__) / "wrapped_token_gateway_v3.json",
        name="WrappedTokenGatewayV3",
    )
    variableDebtUSDC = ContractSpec(
        address="0x5F6f7B0a87CA3CF3d0b431Ae03EF3305180BFf4d",
        abi_path=parent(__file__) / "variableDebt.json",
        name="variableDebtUSDC",
    )
    variableDebtNATIVE = ContractSpec(
        address="0x281963D7471eCdC3A2Bd4503e24e89691cfe420D",
        abi_path=parent(__file__) / "variableDebtNative.json",
        name="variableDebtGnoWxdai",
    )
    variableDebtsDAI = ContractSpec(
        address="0x8Fe06E1D8Aff42Bf6812CacF7854A2249a00bED7",
        abi_path=parent(__file__) / "variableDebt.json",
        name="variableDebtsDAI",
    )
    aUSDC = ContractSpec(
        address="0xc6B7AcA6DE8a6044E0e32d0c841a89244A10D284", abi_path=parent(__file__) / "atoken.json", name="aGnoUSDC"
    )
    aWrappedNative = ContractSpec(
        address="0xd0Dd6cEF72143E22cCED4867eb0d5F2328715533",
        abi_path=parent(__file__) / "aWrappedNative.json",
        name="aGnoWxdai",
    )
    asDAI = ContractSpec(
        address="0x7a5c3860a77a8DC1b225BD46d0fb2ac1C6D191BC", abi_path=parent(__file__) / "atoken.json", name="aGnosDAI"
    )


class OptimismContractSpecs:
    ProtocolDataProvider = ContractSpec(
        address="0x69FA688f1Dc47d4B5d8029D5a35FB7a548310654",
        abi_path=parent(__file__) / "protocol_data_provider.json",
        name="ProtocolDataProvider",
    )
    PoolAddressesProvider = ContractSpec(
        address="0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb",
        abi_path=parent(__file__) / "protocol_address_provider.json",
        name="PoolAddressesProvider",
    )
    LendingPoolV3 = ContractSpec(
        address="0x794a61358D6845594F94dc1DB02A252b5b4814aD",
        abi_path=parent(__file__) / "lending_pool_v3.json",
        name="LendingPoolV3",
    )
    WrappedTokenGatewayV3 = ContractSpec(
        address="0xe9E52021f4e11DEAD8661812A0A6c8627abA2a54",
        abi_path=parent(__file__) / "wrapped_token_gateway_v3.json",
        name="WrappedTokenGatewayV3",
    )
    aUSDC = ContractSpec(
        address="0x625E7708f30cA75bfd92586e17077590C60eb4cD", abi_path=parent(__file__) / "atoken.json", name="aUSDC"
    )
    aUSDCe = ContractSpec(
        address="0x38d693cE1dF5AaDF7bC62595A37D667aD57922e5", abi_path=parent(__file__) / "atoken.json", name="aUSDCe"
    )
    aDAI = ContractSpec(
        address="0x82E64f49Ed5EC1bC6e43DAD4FC8Af9bb3A2312EE", abi_path=parent(__file__) / "atoken.json", name="aDAI"
    )


class ArbitrumContractSpecs:
    ProtocolDataProvider = ContractSpec(
        address="0x69FA688f1Dc47d4B5d8029D5a35FB7a548310654",
        abi_path=parent(__file__) / "protocol_data_provider.json",
        name="ProtocolDataProvider",
    )
    PoolAddressesProvider = ContractSpec(
        address="0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb",
        abi_path=parent(__file__) / "protocol_address_provider.json",
        name="PoolAddressesProvider",
    )
    LendingPoolV3 = ContractSpec(
        address="0x794a61358D6845594F94dc1DB02A252b5b4814aD",
        abi_path=parent(__file__) / "lending_pool_v3.json",
        name="LendingPoolV3",
    )
    WrappedTokenGatewayV3 = ContractSpec(
        address="0xecD4bd3121F9FD604ffaC631bF6d41ec12f1fafb",
        abi_path=parent(__file__) / "wrapped_token_gateway_v3.json",
        name="WrappedTokenGatewayV3",
    )
    aUSDC = ContractSpec(
        address="0x625E7708f30cA75bfd92586e17077590C60eb4cD", abi_path=parent(__file__) / "atoken.json", name="aUSDC"
    )
    aUSDCe = ContractSpec(
        address="0x724dc807b04555b71ed48a6896b6F41593b8C637", abi_path=parent(__file__) / "atoken.json", name="aUSDCe"
    )
    aDAI = ContractSpec(
        address="0x82E64f49Ed5EC1bC6e43DAD4FC8Af9bb3A2312EE", abi_path=parent(__file__) / "atoken.json", name="aDAI"
    )


class BaseContractSpecs:
    ProtocolDataProvider = ContractSpec(
        address="0x2d8A3C5677189723C4cB8873CfC9C8976FDF38Ac",
        abi_path=parent(__file__) / "protocol_data_provider.json",
        name="ProtocolDataProvider",
    )
    PoolAddressesProvider = ContractSpec(
        address="0xe20fCBdBfFC4Dd138cE8b2E6FBb6CB49777ad64D",
        abi_path=parent(__file__) / "protocol_address_provider.json",
        name="PoolAddressesProvider",
    )
    LendingPoolV3 = ContractSpec(
        address="0xA238Dd80C259a72e81d7e4664a9801593F98d1c5",
        abi_path=parent(__file__) / "lending_pool_v3.json",
        name="LendingPoolV3",
    )
    WrappedTokenGatewayV3 = ContractSpec(
        address="0x8be473dCfA93132658821E67CbEB684ec8Ea2E74",
        abi_path=parent(__file__) / "wrapped_token_gateway_v3.json",
        name="WrappedTokenGatewayV3",
    )
    aUSDC = ContractSpec(
        address="0x4e65fE4DbA92790696d040ac24Aa414708F5c0AB", abi_path=parent(__file__) / "atoken.json", name="aUSDC"
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
    Chain.BASE: BaseContractSpecs,
}

Abis = {
    Chain.ETHEREUM: AllAbis,
    Chain.GNOSIS: AllAbis,
    Chain.OPTIMISM: AllAbis,
    Chain.ARBITRUM: AllAbis,
    Chain.BASE: AllAbis,
}
