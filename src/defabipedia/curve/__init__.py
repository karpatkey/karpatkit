from ..types import Chain, ContractSpec, parent

# TODO: check all the ABIs for the different versions of pools, tokens, zaps and gauges...


class GnosisContractSpecs:
    # https://github.com/curvefi/twocrypto-ng/blob/7c97525a9d8ce440bcc224a48724dd4618a44841/contracts/main/CurveTwocryptoOptimized.vy
    GBPe_x3RCV_pool = ContractSpec(
        address="0x0ff26a978a61d40f6591fc700ef878e96af6c2c0",
        abi_path=parent(__file__) / "curve_two_crypto_optimized.json",
        name="gbpe_x3rcv_pool",
    )

    # https://github.com/curvefi/curve-crypto-contract/blob/d7d04cd9ae038970e40be850df99de8c1ff7241b/contracts/two/zaps/ZapTwo.vy
    EURe_x3RCV_deposit_zap = ContractSpec(
        address="0xE3FFF29d4DC930EBb787FeCd49Ee5963DADf60b6",
        abi_path=parent(__file__) / "zap_two.json",
        name="eure_x3rcv_deposit_zap",
    )

    # https://github.com/curvefi/curve-contract/blob/b0bbf77f8f93c9c5f4e415bce9cd71f0cdee960e/contracts/pool-templates/base/SwapTemplateBase.vy
    x3Pool = ContractSpec(
        address="0x7f90122BF0700F9E7e1F688fe926940E8839F353",
        abi_path=parent(__file__) / "swap_template_base.json",
        name="x3pool",
    )


ContractSpecs = {Chain.GNOSIS: GnosisContractSpecs}
