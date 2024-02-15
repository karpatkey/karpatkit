from ..types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    PositionsNFT = ContractSpec(
        address="0xC36442b4a4522E871399CD717aBDD847Ab11FE88",
        abi_path=current_dir() / "positions_nft.json",
        name="positions_nft",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}
