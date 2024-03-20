from ..types import Chain, ContractAbi, ContractSpec, current_dir


# TODO: check all the ABIs for the different versions of pools, tokens, zaps and gauges...

class GnosisContractSpecs:
    GBPe_x3RCV_pool = ContractSpec(
        address="0x0ff26a978a61d40f6591fc700ef878e96af6c2c0", abi_path=current_dir() / "crypto_factory_pool.json",
        name="gbpe_x3rcv_pool"
    )
    EURe_x3RCV_deposit_zap = ContractSpec(
        address="0x0ff26a978a61d40f6591fc700ef878e96af6c2c0", abi_path=current_dir() / "deposit_zap.json",
        name="eure_x3rcv_deposit_zap"
    )


ContractSpecs = {Chain.GNOSIS: GnosisContractSpecs}
