from ..types import Chain, ContractSpec, parent

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
    usdc = ContractSpec(
        address="0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83",
        abi_path=parent(__file__) / "usdc.json",
        name="usdc",
    )



ContractSpecs = {Chain.GNOSIS: GnosisContractSpecs, Chain.ETHEREUM: EthereumContractSpecs}
