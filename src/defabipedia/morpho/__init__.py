from ..types import Chain, ContractAbi, ContractSpec, parent


class AllAbis:
    morpho_vault_v1 = ContractAbi(abi_path=parent(__file__) / "morpho_vault_v1.json", name="morpho_vault_v1")
    morpho_vault_v2 = ContractAbi(abi_path=parent(__file__) / "morpho_vault_v2.json", name="morpho_vault_v2")


class EthereumContractSpecs:
    morpho_blue = ContractSpec(
        address="0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb",
        abi_path=parent(__file__) / "morpho_blue.json",
        name="morpho_blue",
    )
    adaptative_Curve_IRM = ContractSpec(
        address="0x870aC11D48B15DB9a138Cf899d20F13F79Ba00BC",
        abi_path=parent(__file__) / "adaptative_Curve_IRM.json",
        name="adaptative_Curve_IRM",
    )
    oracle_WBTC_USDC = ContractSpec(
        address="0xDddd770BADd886dF3864029e4B377B5F6a2B6b83",
        abi_path=parent(__file__) / "oracle_WBTC_USDC.json",
        name="oracle_WBTC_USDC",
    )
    oracle_wstETH_USDC = ContractSpec(
        address="0x48F7E36EB6B826B2dF4B2E630B62Cd25e89E40e2",
        abi_path=parent(__file__) / "oracle_wstETH_USDC",
        name="oracle_wstETH_USDC",
    )


class BaseContractSpecs:
    morpho_blue = ContractSpec(
        address="0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb",
        abi_path=parent(__file__) / "base_morpho_blue.json",
        name="morpho_blue",
    )
    adaptative_Curve_IRM = ContractSpec(
        address="0x870aC11D48B15DB9a138Cf899d20F13F79Ba00BC",
        abi_path=parent(__file__) / "base_adaptative_Curve_IRM.json",
        name="adaptative_Curve_IRM",
    )

class ArbitrumContractSpecs:
    morpho_blue = ContractSpec(
        address="0x6c247b1F6182318877311737BaC0844bAa518F5e",
        abi_path=parent(__file__) / "morpho_blue.json",
        name="morpho_blue",
    )
    adaptative_Curve_IRM = ContractSpec(
        address="0x66F30587FB8D4206918deb78ecA7d5eBbafD06DA",
        abi_path=parent(__file__) / "adaptative_Curve_IRM.json",
        name="adaptative_Curve_IRM",
    )

class OptimismContractSpecs:
    morpho_blue = ContractSpec(
        address="0xce95AfbB8EA029495c66020883F87aaE8864AF92",
        abi_path=parent(__file__) / "morpho_blue.json",
        name="morpho_blue",
    )
    adaptative_Curve_IRM = ContractSpec(
        address="0x8cD70A8F399428456b29546BC5dBe10ab6a06ef6",
        abi_path=parent(__file__) / "adaptative_Curve_IRM.json",
        name="adaptative_Curve_IRM",
    )

class GnosisContractSpecs:
    morpho_blue = ContractSpec(
        address="0xB74D4dd451E250bC325AFF0556D717e4E2351c66",
        abi_path=parent(__file__) / "morpho_blue.json",
        name="morpho_blue",
    )
    adaptative_Curve_IRM = ContractSpec(
        address="0xae529333703C34b8976BaB9D04AF3f0B9Cff05c5",
        abi_path=parent(__file__) / "adaptative_Curve_IRM.json",
        name="adaptative_Curve_IRM",
    )


ContractSpecs = {Chain.ETHEREUM: EthereumContractSpecs, Chain.BASE: BaseContractSpecs}

Abis = {
    Chain.ETHEREUM: AllAbis,
    Chain.BASE: AllAbis,
}