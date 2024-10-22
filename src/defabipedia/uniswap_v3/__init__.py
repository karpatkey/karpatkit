from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    Pool = ContractAbi(abi_path=parent(__file__) / "pool.json", name="pool")


class EthereumContractSpecs:
    PositionsNFT = ContractSpec(
        address="0xC36442b4a4522E871399CD717aBDD847Ab11FE88",
        abi_path=parent(__file__) / "positions_nft.json",
        name="positions_nft",
    )
    Factory = ContractSpec(
        address="0x1F98431c8aD98523631AE4a59f267346ea31F984", abi_path=parent(__file__) / "factory.json", name="factory"
    )
    UniV3_Quoter = ContractSpec(
        address="0x61fFE014bA17989E743c5F6cB21bF9697530B21e",
        abi_path=parent(__file__) / "quoter_v3.json",
        name="quoter_v3",
    )
    UniV3_SwapRouter = ContractSpec(
        address="0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45",
        abi_path=parent(__file__) / "swap_router_v2.json",
        name="swap_router_v2",
    )
    ApprovePermit2 = ContractSpec(
        address="0x000000000022D473030F116dDEE9F6B43aC78BA3",
        abi_path=parent(__file__) / "approve_permit2.json",
        name="approve_permit2",
    )


class PolygonContractSpecs:
    PositionsNFT = ContractSpec(
        address="0xC36442b4a4522E871399CD717aBDD847Ab11FE88",
        abi_path=parent(__file__) / "positions_nft.json",
        name="positions_nft",
    )
    Factory = ContractSpec(
        address="0x1F98431c8aD98523631AE4a59f267346ea31F984", abi_path=parent(__file__) / "factory.json", name="factory"
    )
    UniV3_Quoter = ContractSpec(
        address="0x61fFE014bA17989E743c5F6cB21bF9697530B21e",
        abi_path=parent(__file__) / "quoter_v3.json",
        name="quoter_v3",
    )
    UniV3_SwapRouter = ContractSpec(
        address="0xE592427A0AEce92De3Edee1F18E0157C05861564",
        abi_path=parent(__file__) / "swap_router_v3.json",
        name="swap_router_v3",
    )


class GnosisContractSpecs:
    PositionsNFT = ContractSpec(
        address="0xAE8fbE656a77519a7490054274910129c9244FA3",
        abi_path=parent(__file__) / "positions_nft.json",
        name="positions_nft",
    )
    Factory = ContractSpec(
        address="0xe32F7dD7e3f098D518ff19A22d5f028e076489B1", abi_path=parent(__file__) / "factory.json", name="factory"
    )
    UniV3_Quoter = ContractSpec(
        address="0x7E9cB3499A6cee3baBe5c8a3D328EA7FD36578f4",
        abi_path=parent(__file__) / "quoter_v3.json",
        name="quoter_v3",
    )
    UniV2_SwapRouter = ContractSpec(
        address="0xc6D25285D5C5b62b7ca26D6092751A145D50e9Be",
        abi_path=parent(__file__) / "swap_router_v2.json",
        name="swap_router_v2",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.POLYGON: PolygonContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
}

Abis = {Chain.ETHEREUM: AllAbis, Chain.POLYGON: AllAbis, Chain.GNOSIS: AllAbis}
