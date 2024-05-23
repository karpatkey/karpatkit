from ..types import Chain, ContractSpec, current_dir


class ArbitrumContractSpecs:
    DolomiteMargin = ContractSpec(
        address="0x6Bd780E7fDf01D77e4d475c821f1e7AE05409072",
        abi_path=current_dir() / "dolomite_margin.json",
        name="dolomite_margin",
    )

    BorrowProxyV2 = ContractSpec(
        address="0x38E49A617305101216eC6306e3a18065D14Bf3a7",
        abi_path="",
        name="borrow_proxy_v2",
    )


ContractSpecs = {Chain.ARBITRUM: ArbitrumContractSpecs}
