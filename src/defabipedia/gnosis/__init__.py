from ..types import Chain, ContractSpec, current_dir


class GnosisContractSpecs:
    sDAI = ContractSpec(
        address="0xaf204776c7245bF4147c2612BF6e5972Ee483701", abi_path=current_dir() / "sdai.json", name="sdai"
    )


ContractSpecs = {Chain.GNOSIS: GnosisContractSpecs}
