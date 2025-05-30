from ..types import Chain, ContractSpec, parent

class ArbitrumContractSpecs:
    Datastore = ContractSpec(
        address="0xFD70de6b91282D8017aA4E741e9Ae325CAb992d8",
        abi_path=parent(__file__) / "datastore.json",
        name="datastore",
    )

    Exchange_router = ContractSpec(
        address="0xE3FFF29d4DC930EBb787FeCd49Ee5963DADf60b6",
        abi_path=parent(__file__) / "exchange_router.json",
        name="exchange_router",
    )

    Reader = ContractSpec(
        address="0x7f90122BF0700F9E7e1F688fe926940E8839F353",
        abi_path=parent(__file__) / "reader.json",
        name="reader",
    )



ContractSpecs = {Chain.ARBITRUM: ArbitrumContractSpecs}