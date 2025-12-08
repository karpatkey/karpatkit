from defabipedia.types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall3.json",
        name="multicall3",
    )
    MultisendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )


class GnosisContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall3.json",
        name="multicall3",
    )
    MultisendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )


class OptimismContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",
        abi_path=parent(__file__) / "multicall3.json",
        name="multicall3",
    )
    MultisendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )


class ArbitrumContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",  # multicall2 instead of multicall but fine
        abi_path=parent(__file__) / "multicall3.json",
        name="multical3",
    )
    MultisendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )


class BaseContractSpecs:
    Multicall = ContractSpec(
        address="0xcA11bde05977b3631167028862bE2a173976CA11",  # multicall2 instead of multicall but fine
        abi_path=parent(__file__) / "multicall3.json",
        name="multical3",
    )
    MultisendCallOnly = ContractSpec(
        address="0xA83c336B20401Af773B6219BA5027174338D1836",
        abi_path=parent(__file__) / "multisend_call_only.json",
        name="multisend_call_only",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
    Chain.BASE: BaseContractSpecs,
}
