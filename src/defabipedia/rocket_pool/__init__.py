from defabipedia.types import Chain, ContractAbi, ContractSpec, parent


class EthereumContractSpecs:
    Storage = ContractSpec(
        address="0x1d8f8f00cfa6758d7bE78336684788Fb0ee0Fa46", abi_path=parent(__file__) / "storage.json", name="Storage"
    )
    SwapRouter = ContractSpec(
        address="0x16D5A408e807db8eF7c578279BEeEe6b228f1c1C",
        abi_path=parent(__file__) / "swap_router.json",
        name="SwapRouter",
    )
    rETH = ContractSpec(
        address="0xae78736Cd615f374D3085123A210448E74Fc6393", abi_path=parent(__file__) / "rETH.json", name="rETH"
    )


class EthereumAbis:
    DepositPool = ContractAbi(abi_path=parent(__file__) / "deposit_pool.json", name="DepositPool")
    ProtocolSettingsDeposit = ContractAbi(
        abi_path=parent(__file__) / "protocol_settings_deposit.json", name="ProtocolSettingsDeposit"
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs}

Abis = {Chain.ETHEREUM: EthereumAbis}
