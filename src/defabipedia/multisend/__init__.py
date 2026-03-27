from defabipedia.types import Chain, ContractSpec, parent


class AllAbis:
    pass


class EthereumContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )
    MultiSendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )

    MultiCall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall.json",
        name="MultiCall",
    )


class GnosisContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )
    MultiSendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )

    MultiCall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall.json",
        name="MultiCall",
    )


class OptimismContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )
    MultiSendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )

    MultiCall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall.json",
        name="MultiCall",
    )


class ArbitrumContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )
    MultiSendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )

    MultiCall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall.json",
        name="MultiCall",
    )


class BaseContractSpecs:
    MultiSend = ContractSpec(
        address="0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526",
        abi_path=parent(__file__) / "multisend.json",
        name="MultiSend",
    )
    MultiSendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )

    MultiCall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall.json",
        name="MultiCall",
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
