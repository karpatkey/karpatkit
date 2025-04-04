from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    PriceOracle = ContractAbi(abi_path=parent(__file__) / "price_oracle.json", name="price_oracle")
    LendingPool = ContractAbi(abi_path=parent(__file__) / "lending_pool.json", name="lending_pool")


class EthereumContractSpecs:
    ProtocolDataProvider = ContractSpec(
        address="0xFc21d6d146E6086B8359705C8b28512a983db0cb",
        abi_path=parent(__file__) / "protocol_data_provider.json",
        name="protocol_data_provider",
    )
    PoolAddressesProvider = ContractSpec(
        address="0x02C3eA4e34C0cBd694D2adFa2c690EECbC1793eE",
        abi_path=parent(__file__) / "pool_addresses_provider.json",
        name="pool_addresses_provider",
    )
    LendingPoolV3 = ContractSpec(
        address="0xC13e21B648A5Ee794902342038FF3aDAB66BE987",
        abi_path=parent(__file__) / "lending_pool.json",
        name="LendingPoolV3",
    )
    spWrappedNative = ContractSpec(
        address="0x59cD1C87501baa753d0B5B5Ab5D8416A45cD71DB",
        abi_path=parent(__file__) / "spWrappedNative.json",
        name="spEthWeth",
    )
    WrappedTokenGatewayV3 = ContractSpec(
        address="0xBD7D6a9ad7865463DE44B05F04559f65e3B11704",
        abi_path=parent(__file__) / "wrapped_token_gateway_v3.json",
        name="WrappedTokenGatewayV3",
    )
    variableDebtNATIVE = ContractSpec(
        address="0x2e7576042566f8D6990e07A1B61Ad1efd86Ae70d",
        abi_path=parent(__file__) / "variableDebtNative.json",
        name="variableDebtEthWeth",
    )
    sDAI = ContractSpec(
        address="0x83F20F44975D03b1b09e64809B757c47f942BEeA",
        abi_path=parent(__file__) / "sdai.json",
        name="sdai",
    )
    spDAI = ContractSpec(
        address="0x4DEDf26112B3Ec8eC46e7E31EA5e123490B05B8B",
        abi_path=parent(__file__) / "sptoken.json",
        name="spDAI",
    )
    variableDebtDAI = ContractSpec(
        address="0xf705d2B7e92B3F38e6ae7afaDAA2fEE110fE5914",
        abi_path=parent(__file__) / "variable_debt_token.json",
        name="variableDebtDAI",
    )
    spUSDC = ContractSpec(
        address="0x377C3bd93f2a2984E1E7bE6A5C22c525eD4A4815",
        abi_path=parent(__file__) / "sptoken.json",
        name="spUSDC",
    )
    variableDebtUSDC = ContractSpec(
        address="0x7B70D04099CB9cfb1Db7B6820baDAfB4C5C70A67",
        abi_path=parent(__file__) / "variable_debt_token.json",
        name="variableDebtUSDC",
    )


class GnosisContractSpecs:
    ProtocolDataProvider = ContractSpec(
        address="0x2a002054A06546bB5a264D57A81347e23Af91D18",
        abi_path=parent(__file__) / "protocol_data_provider.json",
        name="protocol_data_provider",
    )
    PoolAddressesProvider = ContractSpec(
        address="0xA98DaCB3fC964A6A0d2ce3B77294241585EAbA6d",
        abi_path=parent(__file__) / "pool_addresses_provider.json",
        name="pool_addresses_provider",
    )
    LendingPoolV3 = ContractSpec(
        address="0x2Dae5307c5E3FD1CF5A72Cb6F698f915860607e0",
        abi_path=parent(__file__) / "lending_pool.json",
        name="LendingPoolV3",
    )
    sDAI = ContractSpec(
        address="0xaf204776c7245bF4147c2612BF6e5972Ee483701",
        abi_path=parent(__file__) / "sdai.json",
        name="sdai",
    )
    spsDAI = ContractSpec(
        address="0xE877b96caf9f180916bF2B5Ce7Ea8069e0123182",
        abi_path=parent(__file__) / "sptoken.json",
        name="spsDAI",
    )
    WrappedTokenGatewayV3 = ContractSpec(
        address="0xBD7D6a9ad7865463DE44B05F04559f65e3B11704",
        abi_path=parent(__file__) / "wrapped_token_gateway_v3.json",
        name="WrappedTokenGatewayV3",
    )
    variableDebtNATIVE = ContractSpec(
        address="0x868ADfDf12A86422524EaB6978beAE08A0008F37",
        abi_path=parent(__file__) / "variableDebtNative.json",
        name="variableDebtDAI",
    )
    variableDebtUSDC = ContractSpec(
        address="0xBC4f20DAf4E05c17E93676D2CeC39769506b8219",
        abi_path=parent(__file__) / "variable_debt_token.json",
        name="variableDebtUSDC",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}

Abis = {Chain.ETHEREUM: AllAbis, Chain.GNOSIS: AllAbis}
