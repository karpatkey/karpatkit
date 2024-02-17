from ..types import Chain, ContractSpec, ContractAbi, current_dir

class AllAbis:
    Pool = ContractAbi(
        abi_path=current_dir() / "pool.json", name="pool"
    )

class EthereumContractSpecs:
    PositionsNFT = ContractSpec(
        address="0xC36442b4a4522E871399CD717aBDD847Ab11FE88", abi_path=current_dir() / "positions_nft.json", name="positions_nft"
    )
    Factory = ContractSpec(
        address="0x1F98431c8aD98523631AE4a59f267346ea31F984", abi_path=current_dir() / "factory.json", name="factory"
    )

ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}

Abis = {Chain.ETHEREUM: AllAbis}