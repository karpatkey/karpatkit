from ..types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    PositionsNFT = ContractSpec(
        address="0xC36442b4a4522E871399CD717aBDD847Ab11FE88",
        abi_path=current_dir() / "positions_nft.json",
        name="positions_nft",
    )
    UniV3_Quoter = ContractSpec(
        address="0x61fFE014bA17989E743c5F6cB21bF9697530B21e",
        abi_path=current_dir() / "quoter_v3.json",
        name="quoter_v3",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
