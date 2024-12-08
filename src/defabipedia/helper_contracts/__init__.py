from ..types import Chain, ContractAbi, ContractSpec, parent


class EthereumContractSpecs:
    BalanceScanner = ContractSpec(
        address="0x54eCF3f6f61F63fdFE7c27Ee8A86e54899600C92",
        abi_path=parent(__file__) / "balance_scanner.json",
        name="balance_scanner",
    )


class GnosisContractSpecs:
    BalanceScanner = ContractSpec(
        address="0x54eCF3f6f61F63fdFE7c27Ee8A86e54899600C92",
        abi_path=parent(__file__) / "balance_scanner.json",
        name="balance_scanner",
    )


class OptimismContractSpecs:
    BalanceScanner = ContractSpec(
        address="0x54eCF3f6f61F63fdFE7c27Ee8A86e54899600C92",
        abi_path=parent(__file__) / "balance_scanner.json",
        name="balance_scanner",
    )


class ArbitrumContractSpecs:
    BalanceScanner = ContractSpec(
        address="0x54eCF3f6f61F63fdFE7c27Ee8A86e54899600C92",
        abi_path=parent(__file__) / "balance_scanner.json",
        name="balance_scanner",
    )


class BaseContractSpecs:
    BalanceScanner = ContractSpec(
        address="0x54eCF3f6f61F63fdFE7c27Ee8A86e54899600C92",
        abi_path=parent(__file__) / "balance_scanner.json",
        name="balance_scanner",
    )


class PolygonContractSpecs:
    BalanceScanner = ContractSpec(
        address="0x54eCF3f6f61F63fdFE7c27Ee8A86e54899600C92",
        abi_path=parent(__file__) / "balance_scanner.json",
        name="balance_scanner",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.GNOSIS: GnosisContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
    Chain.BASE: BaseContractSpecs,
    Chain.POLYGON: PolygonContractSpecs,
}
