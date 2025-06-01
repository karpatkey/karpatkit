from ..types import Chain, ContractSpec, parent


class ArbitrumContractSpecs:
    Datastore = ContractSpec(
        address="0xFD70de6b91282D8017aA4E741e9Ae325CAb992d8",
        abi_path=parent(__file__) / "datastore.json",
        name="datastore",
    )

    Exchange_router = ContractSpec(
        address="0x5aC4e27341e4cCcb3e5FD62f9E62db2Adf43dd57",
        abi_path=parent(__file__) / "exchange_router.json",
        name="exchange_router",
    )

    Reader = ContractSpec(
        address="0x0537C767cDAC0726c76Bb89e92904fe28fd02fE1",
        abi_path=parent(__file__) / "reader.json",
        name="reader",
    )

    Order_vault = ContractSpec(
        address="0x31eF83a530Fde1B38EE9A18093A333D8Bbbc40D5",
        abi_path=parent(__file__) / "order_vault.json",
        name="order_vault",
    )


ContractSpecs = {Chain.ARBITRUM: ArbitrumContractSpecs}
