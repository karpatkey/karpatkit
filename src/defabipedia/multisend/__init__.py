from defabipedia.types import Chain, ContractSpec, current_dir


class AllAbis:
    pass


class EthereumContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=current_dir() / "multisend.json",
        name="MultiSend",
    )


class GnosisContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=current_dir() / "multisend.json",
        name="MultiSend",
    )


class OptimismContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=current_dir() / "multisend.json",
        name="MultiSend",
    )


class ArbitrumContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=current_dir() / "multisend.json",
        name="MultiSend",
    )


class BaseContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=current_dir() / "multisend.json",
        name="MultiSend",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
    Chain.BASE: BaseContractSpecs,
}

Abis = {
    Chain.ETHEREUM: AllAbis,
    Chain.GNOSIS: AllAbis,
    Chain.OPTIMISM: AllAbis,
    Chain.ARBITRUM: AllAbis,
    Chain.BASE: AllAbis,
}
