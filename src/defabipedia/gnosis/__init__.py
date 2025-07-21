from ..types import Chain, ContractAbi, ContractSpec, parent


class GnosisAbis:
    asset_gno = ContractAbi(abi_path=parent(__file__) / "asset_gno.json", name="asset_gno")


class EthereumContractSpecs:
    amb_eth_xdai = ContractSpec(
        address="0x4C36d2919e407f0Cc2Ee3c993ccF8ac26d9CE64e",
        abi_path=parent(__file__) / "amb_eth_xdai.json",
        name="amb_eth_xdai",
    )


class GnosisContractSpecs:
    sDAI = ContractSpec(
        address="0xaf204776c7245bF4147c2612BF6e5972Ee483701", abi_path=parent(__file__) / "sdai.json", name="sdai"
    )


ContractSpecs = {Chain.GNOSIS: GnosisContractSpecs, Chain.ETHEREUM: EthereumContractSpecs}
Abis = {
    Chain.GNOSIS: GnosisAbis,
}