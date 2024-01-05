from ..types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    CowswapSigner = ContractSpec(
        address="0x23dA9AdE38E4477b23770DeD512fD37b12381FAB",
        abi_path=current_dir() / "cowswap_signer.json",
        name="cowswap_signer",
    )


class GnosisContractSpecs:
    CowswapSigner = ContractSpec(
        address="0x23dA9AdE38E4477b23770DeD512fD37b12381FAB",
        abi_path=current_dir() / "cowswap_signer.json",
        name="cowswap_signer",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.GNOSIS: GnosisContractSpecs}
