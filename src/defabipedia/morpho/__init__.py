from ..types import Chain, ContractSpec, current_dir


class EthereumContractSpecs:
    morpho_blue = ContractSpec(
        address="0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb",
        abi_path=current_dir() / "morpho_blue.json",
        name="morpho_blue",
    )
    adaptative_Curve_IRM = ContractSpec(
        address="0x870aC11D48B15DB9a138Cf899d20F13F79Ba00BC",
        abi_path=current_dir() / "adaptative_Curve_IRM.json",
        name="adaptative_Curve_IRM",
    )
    oracle_WBTC_USDC = ContractSpec(
        address="0xDddd770BADd886dF3864029e4B377B5F6a2B6b83",
        abi_path=current_dir() / "oracle_WBTC_USDC.json",
        name="oracle_WBTC_USDC",
    )
    oracle_wstETH_USDC = ContractSpec(
        address="0x48F7E36EB6B826B2dF4B2E630B62Cd25e89E40e2",
        abi_path=current_dir() / "oracle_wstETH_USDC",
        name="oracle_wstETH_USDC",
    )

class BaseContractSpecs:
    morpho_blue = ContractSpec(
        address="0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb",
        abi_path=current_dir() / "base_morpho_blue.json",
        name="morpho_blue",
    )
    adaptative_Curve_IRM = ContractSpec(
        address="0x870aC11D48B15DB9a138Cf899d20F13F79Ba00BC",
        abi_path=current_dir() / "base_adaptative_Curve_IRM.json",
        name="adaptative_Curve_IRM",
    )
    
ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.BASE: BaseContractSpecs}
