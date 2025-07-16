from defabipedia.types import Chain, ContractSpec, parent


class EthereumContractSpecs:
    TokenMessengerv1 = ContractSpec(
        address="0xBd3fa81B58Ba92a82136038B25aDec7066af3155",
        abi_path=parent(__file__) / "token_messenger.json",
        name="TokenMessenger",
    )
    MessageTransmitterv1 = ContractSpec(
        address="0x0a992d191DEeC32aFe36203Ad87D7d289a738F81",
        abi_path=parent(__file__) / "message_transmitter.json",
        name="MessageTransmitter",
    )


class ArbitrumContractSpecs:
    TokenMessengerv1 = ContractSpec(
        address="0x19330d10D9Cc8751218eaf51E8885D058642E08A",
        abi_path=parent(__file__) / "token_messenger.json",
        name="TokenMessenger",
    )
    MessageTransmitterv1 = ContractSpec(
        address="0xC30362313FBBA5cf9163F0bb16a0e01f01A896ca",
        abi_path=parent(__file__) / "message_transmitter.json",
        name="MessageTransmitter",
    )


class BaseContractSpecs:
    TokenMessengerv1 = ContractSpec(
        address="0x1682Ae6375C4E4A97e4B583BC394c861A46D8962",
        abi_path=parent(__file__) / "token_messenger.json",
        name="TokenMessenger",
    )
    MessageTransmitterv1 = ContractSpec(
        address="0xAD09780d193884d503182aD4588450C416D6F9D4",
        abi_path=parent(__file__) / "message_transmitter.json",
        name="MessageTransmitter",
    )


class OptimismContractSpecs:
    TokenMessengerv1 = ContractSpec(
        address="0x2B4069517957735bE00ceE0fadAE88a26365528f",
        abi_path=parent(__file__) / "token_messenger.json",
        name="TokenMessenger",
    )
    MessageTransmitterv1 = ContractSpec(
        address="0x4D41f22c5a0e5c74090899E5a8Fb597a8842b3e8",
        abi_path=parent(__file__) / "message_transmitter.json",
        name="MessageTransmitter",
    )


ContractSpecs = {
    Chain.ETHEREUM: EthereumContractSpecs,
    Chain.OPTIMISM: OptimismContractSpecs,
    Chain.ARBITRUM: ArbitrumContractSpecs,
    Chain.BASE: BaseContractSpecs,
}
