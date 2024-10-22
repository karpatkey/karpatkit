from ..types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    CowswapSigner = ContractSpec(
        address="0x23dA9AdE38E4477b23770DeD512fD37b12381FAB",
        abi_path=parent(__file__) / "cowswap_signer.json",
        name="cowswap_signer",
    )
    CowswapRelayer = ContractSpec(
        address="0xC92E8bdf79f0507f65a392b0ab4667716BFE0110",
        abi_path=parent(__file__) / "cowswap_relayer.json",
        name="cowswap_relayer",
    )


class GnosisContractSpecs:
    CowswapSigner = ContractSpec(
        address="0x23dA9AdE38E4477b23770DeD512fD37b12381FAB",
        abi_path=parent(__file__) / "cowswap_signer.json",
        name="cowswap_signer",
    )
    CowswapRelayer = ContractSpec(
        address="0xC92E8bdf79f0507f65a392b0ab4667716BFE0110",
        abi_path=parent(__file__) / "cowswap_relayer.json",
        name="cowswap_relayer",
    )


class ArbitrumContractSpecs:
    CowswapSigner = ContractSpec(
        address="0x23dA9AdE38E4477b23770DeD512fD37b12381FAB",
        abi_path=parent(__file__) / "cowswap_signer.json",
        name="cowswap_signer",
    )
    CowswapRelayer = ContractSpec(
        address="0xC92E8bdf79f0507f65a392b0ab4667716BFE0110",
        abi_path=parent(__file__) / "cowswap_relayer.json",
        name="cowswap_relayer",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
}
