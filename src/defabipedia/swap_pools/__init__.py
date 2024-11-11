from ..types import Chain, SwapPools, parent


class EthereumSwapPools:
    TriPool = SwapPools(
        address="0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7",
        abi_path=parent(__file__) / "tri_pool.json",
        name="tri_pool",
        tokens=[
            "0x6B175474E89094C44Da98b954EedeAC495271d0F",
            "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        ],
        protocol="Curve",
    )
    Curve_stETH_ETH = SwapPools(
        address="0xDC24316b9AE028F1497c275EB9192a3Ea0f67022",
        abi_path=parent(__file__) / "stETH_ETH_pool_curve.json",
        name="stETH_ETH_pool_curve",
        tokens=["0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"],
        protocol="Curve",
    )
    Curve_oETH_ETH = SwapPools(
        address="0x94b17476a93b3262d87b9a326965d1e91f9c13e7",
        abi_path=parent(__file__) / "oETH_ETH_pool_curve.json",
        name="oETH_ETH_pool_curve",
        tokens=["0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", "0x856c4Efb76C1D1AE02e20CEB03A2A6a08b0b8dC3"],
        protocol="Curve",
    )

    Curve_osETH_rETH = SwapPools(
        address="0xe080027Bd47353b5D1639772b4a75E9Ed3658A0d",
        abi_path=parent(__file__) / "osETH_rETH_pool_curve.json",
        name="osETH_rETH_pool_curve",
        tokens=["0xf1C9acDc66974dFB6dEcB12aA385b9cD01190E38", "0xae78736Cd615f374D3085123A210448E74Fc6393"],
        protocol="Curve",
    )
    Curve_stETH_ETH2 = SwapPools(
        address="0x21E27a5E5513D6e65C4f830167390997aA84843a",
        abi_path=parent(__file__) / "stETH_ETH_poo2_curve.json",
        name="stETH_ETH_pool2_curve",
        tokens=["0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"],
        protocol="Curve",
    )
    UniV3_USDC_ETH = SwapPools(
        address="0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640",
        abi_path=parent(__file__) / "USDC_ETH_pool.json",
        name="USDC_ETH_pool",
        tokens=["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
        protocol="UniswapV3",
        uni_fee=500,
    )
    UniV3_USDC_ETH2 = SwapPools(
        address="0x5FbDB2315678afecb367f032d93F642f64180aa3",
        abi_path=parent(__file__) / "USDC_ETH_pool_2.json",
        name="USDC_ETH_pool_2",
        tokens=["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
        protocol="UniswapV3",
        uni_fee=3000,
    )
    UniV3_USDT_ETH = SwapPools(
        address="0x4e68Ccd3E89f51C3074ca5072bbAC773960dFa36",
        abi_path=parent(__file__) / "USDT_ETH_pool.json",
        name="USDT_ETH_pool",
        tokens=["0xdAC17F958D2ee523a2206206994597C13D831ec7", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
        protocol="UniswapV3",
        uni_fee=3000,
    )
    UniV3_USDT_ETH2 = SwapPools(
        address="0x7aF4D4d3cD5BfCfD9dCf4cEe8d7f7aA1b7e2bC0A",
        abi_path=parent(__file__) / "USDT_ETH_pool_2.json",
        name="USDT_ETH_pool_2",
        tokens=["0xdAC17F958D2ee523a2206206994597C13D831ec7", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
        protocol="UniswapV3",
        uni_fee=500,
    )
    UniV3_USDC_USDT = SwapPools(
        address="0x3416cF6C708Da44DB2624D63ea0AAef7113527C6",
        abi_path=parent(__file__) / "USDC_USDT_pool.json",
        name="USDC_USDT_pool",
        tokens=["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "0xdAC17F958D2ee523a2206206994597C13D831ec7"],
        protocol="UniswapV3",
    )
    UniV3_DAI_USDC = SwapPools(
        address="0x5777d92f208679DB4b9778590Fa3CAB3aC9e2168",
        abi_path=parent(__file__) / "DAI_USDC_pool.json",
        name="DAI_USDC_pool",
        tokens=["0x6B175474E89094C44Da98b954EedeAC495271d0F", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"],
        protocol="UniswapV3",
    )
    UniV3_wstETH_ETH = SwapPools(
        address="0x109830a1AAaD605BbF02a9dFA7B0B92EC2FB7dAa",
        abi_path=parent(__file__) / "wstETH_ETH_pool.json",
        name="wstETH_ETH_pool",
        tokens=["0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
        protocol="UniswapV3",
    )
    UniV3_DAI_USDC2 = SwapPools(
        address="0x6c6Bc977E13Df9b0de53b251522280BB72383700",
        abi_path=parent(__file__) / "DAI_USDC_pool_2.json",
        name="DAI_USDC_pool_2",
        tokens=["0x6B175474E89094C44Da98b954EedeAC495271d0F", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"],
        protocol="UniswapV3",
        uni_fee=500,
    )
    bal_rETH_WETH = SwapPools(
        address="0x1E19CF2D73a72Ef1332C882F20534B6519Be0276",
        abi_path=parent(__file__) / "rETH_WETH_pool.json",
        name="rETH_WETH_pool",
        tokens=["0xae78736Cd615f374D3085123A210448E74Fc6393", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
        protocol="Balancer",
    )
    bal_wstETH_WETH2 = SwapPools(
        address="0x93d199263632a4EF4Bb438F1feB99e57b4b5f0BD",
        abi_path=parent(__file__) / "bal_wstETH_WETH_pool.json",
        name="bal_wstETH_WETH_pool",
        tokens=["0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"],
        protocol="Balancer",
    )

    bal_GYD_USDT = SwapPools(
        address="0xfbfaD5fa9E99081da6461F36f229B5cC88A64c63",
        abi_path=parent(__file__) / "bal_GYD_USDT_pool.json",
        name="ECLP-GYD-USDT",
        tokens=["0xdAC17F958D2ee523a2206206994597C13D831ec7", "0xe07F9D810a48ab5c3c914BA3cA53AF14E4491e8A"],
        protocol="Balancer",
    )
    bal_GYD_sDAI = SwapPools(
        address="0x2191Df821C198600499aA1f0031b1a7514D7A7D9",
        abi_path=parent(__file__) / "bal_GYD_sDAI_pool.json",
        name="ECLP-GYD-sDAI",
        tokens=["0xdAC17F958D2ee523a2206206994597C13D831ec7", "0xe07F9D810a48ab5c3c914BA3cA53AF14E4491e8A"],
        protocol="Balancer",
    )
    bal_GYD_sDAI2 = SwapPools(
        address="0x1CCE5169bDe03f3d5aD0206f6BD057953539DAE6",
        abi_path=parent(__file__) / "bal_GYD_sDAI_pool2.json",
        name="ECLP-GYD-sDAI",
        tokens=["0xdAC17F958D2ee523a2206206994597C13D831ec7", "0xe07F9D810a48ab5c3c914BA3cA53AF14E4491e8A"],
        protocol="Balancer",
    )
    bal_GYD_USDC = SwapPools(
        address="0xC2AA60465BfFa1A88f5bA471a59cA0435c3ec5c1",
        abi_path=parent(__file__) / "bal_GYD_USDC_pool.json",
        name="ECLP-GYD-USDC",
        tokens=["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "0xe07F9D810a48ab5c3c914BA3cA53AF14E4491e8A"],
        protocol="Balancer",
    )
    bal_GYD_GHO = SwapPools(
        address="0xaA7a70070E7495fe86c67225329DbD39BAa2F63b",
        abi_path=parent(__file__) / "bal_GYD_GHO_pool.json",
        name="ECLP-GHO-GYD",
        tokens=["0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f", "0xe07F9D810a48ab5c3c914BA3cA53AF14E4491e8A"],
        protocol="Balancer",
    )
    bal_GHO_USDT_USDC = SwapPools(
        address="0x8353157092ED8Be69a9DF8F95af097bbF33Cb2aF",
        abi_path=parent(__file__) / "bal_GHO_USDT_USDC_pool.json",
        name="GHO/USDT/USDC",
        tokens=[
            "0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f",
            "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        ],
        protocol="Balancer",
    )


class GnosisSwapPools:
    TriPool = SwapPools(
        address="0x7f90122BF0700F9E7e1F688fe926940E8839F353",
        abi_path=parent(__file__) / "tri_pool_gc.json",
        name="tri_pool_gc",
        tokens=[
            "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
            "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83",
            "0x4ECaBa5870353805a9F068101A40E0f32ed605C6",
        ],
        protocol="Curve",
    )
    Curve_EURe_tripool = SwapPools(
        address="0x056c6c5e684cec248635ed86033378cc444459b0",
        abi_path=parent(__file__) / "EURe_tripool_pool.json",
        name="EURe_tripool_pool",
        tokens=[
            "0xcB444e90D8198415266c6a2724b7900fb12FC56E",
            "0x1337BedC9D22ecbe766dF105c9623922A27963EC",
        ],
        protocol="Curve",
    )
    bal_wstETH_WETH_pool = SwapPools(
        address="0xbAd20c15A773bf03ab973302F61FAbceA5101f0A",
        abi_path=parent(__file__) / "bal_wstETH_WETH_pool.json",
        name="bal_wstETH_WETH_pool",
        tokens=["0x6C76971f98945AE98dD7d4DFcA8711ebea946eA6", "0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1"],
        protocol="Balancer",
    )
    bal_USDT_USDC_sDAI_pool = SwapPools(
        address="0x7644fA5D0eA14FcF3E813Fdf93ca9544f8567655",
        abi_path=parent(__file__) / "bal_USDT_USDC_sDAI_pool.json",
        name="bal_USDT_USDC_sDAI_pool",
        tokens=[
            "0x4ECaBa5870353805a9F068101A40E0f32ed605C6",
            "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83",
            "0xaf204776c7245bF4147c2612BF6e5972Ee483701",
        ],
        protocol="Balancer",
    )
    bal_stable_usd_pool = SwapPools(
        address="0x2086f52651837600180dE173B09470F54EF74910",
        abi_path=parent(__file__) / "bal_stable_usd_pool.json",
        name="bal_stable_usd_pool",
        tokens=[
            "0x4ECaBa5870353805a9F068101A40E0f32ed605C6",
            "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83",
            "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
        ],
        protocol="Balancer",
    )
    bal_stable_wstETH_pool = SwapPools(
        address="0xEb30C85CC528537f5350CF5684Ce6a4538e13394",
        abi_path=parent(__file__) / "bal_stabal_wstETH_pool.json",
        name="bal_stabal_wstETH_pool",
        tokens=["0x6C76971f98945AE98dD7d4DFcA8711ebea946eA6", "0x2086f52651837600180dE173B09470F54EF74910"],
        protocol="Balancer",
    )
    Uni_USDC_WETH_pool = SwapPools(
        address="0x9ac75f5E0e3388Da18D9Ea214Ed9f3AAcfa66A1D",
        abi_path=parent(__file__) / "Uni_USDC_WETH_pool.json",
        name="Uni_USDC_WETH_pool",
        tokens=["0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1", "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83"],
        protocol="UniswapV3",
        uni_fee=3000,
    )


SwapPoolInstances = {Chain.ETHEREUM: EthereumSwapPools, Chain.GNOSIS: GnosisSwapPools}
