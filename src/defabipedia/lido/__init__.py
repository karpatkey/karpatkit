from ..types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    stETH = ContractSpec(
        address="0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84", abi_path=parent(__file__) / "steth.json", name="steth"
    )
    wstETH = ContractSpec(
        address="0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0", abi_path=parent(__file__) / "wsteth.json", name="wsteth"
    )
    unstETH = ContractSpec(
        address="0x889edC2eDab5f40e902b864aD4d7AdE8E412F9B1", abi_path=parent(__file__) / "unsteth.json", name="unsteth"
    )
    trpEscrowProto = ContractSpec(
        address="0x484FD04c598A095360DF89bF85AB34c37127AA39",
        abi_path=parent(__file__) / "trp_escrow_proto.json",
        name="trpEscrowProto",
    )


class GnosisContractSpecs:
    # TODO not available at this point in gc
    # stETH = ContractSpec(address='0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84',
    #                                     abi=load_abi('steth.json'),
    #                                     name='steth')
    wstETH = ContractSpec(
        address="0x6C76971f98945AE98dD7d4DFcA8711ebea946eA6", abi_path=parent(__file__) / "wsteth.json", name="wsteth"
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}
