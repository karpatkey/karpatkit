import json

from eth_typing import AnyAddress
from web3 import Web3, contract

from ..types import Chain, ContractAbi, ContractSpec, current_dir

with open(current_dir() / "erc20.json") as f:
    ERC20_ABI = json.load(f)


def erc20_contract(w3: Web3, address: AnyAddress) -> contract.Contract:
    """Construct a generic ERC-20 token contract instance from the address."""
    return w3.eth.contract(address=address, abi=ERC20_ABI)


NATIVE = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"  # Native asset convention for every chain (EIP-7528)


class Abis:
    ERC20 = ContractAbi(abi=ERC20_ABI, name="erc20")


class EthereumTokenAddr:
    AAVE = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
    ABPT = "0x41A08648C3766F9F9d85598fF102a08f4ef84F84"
    AURA = "0xC0c293ce456fF0ED870ADd98a0828Dd4d2903DBF"
    auraBAL = "0x616e8BfA43F920657B3497DBf40D6b1A02D4608d"
    AURABAL = "0x616e8BfA43F920657B3497DBf40D6b1A02D4608d"
    BAL = "0xba100000625a3754423978a60c9317c58a424e3D"
    BAT = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
    BB_A_USD = "0xA13a9247ea42D743238089903570127DdA72fE44"
    BB_A_USD_OLD = "0x7B50775383d3D6f0215A8F290f2C9e2eEBBEceb2"
    BB_A_USD_V3 = "0xfeBb0bbf162E64fb9D0dfe186E517d84C395f016"
    BNT = "0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C"
    COMP = "0xc00e94Cb662C3520282E6f5717214004A7f26888"
    COW = "0xDEf1CA1fb7FBcDC777520aa7f396b4E015F497aB"
    CRV = "0xD533a949740bb3306d119CC777fa900bA034cd52"
    cUSDCv3 = "0xc3d688B66703497DAA19211EEdff47f25384cdc3"
    CVX = "0x4e3FBD56CD56c3e72c1403e103b45Db9da5B9D2B"
    CVXCRV = "0x62B9c7356A2Dc64a1969e19C23e4f579F9810Aa7"
    cWETHv3 = "0xA17581A9E3356d9A858b789D68B4d866e593aE94"
    DAI = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
    E = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
    eETH = "0x35fA164735182de50811E8e2E824cFb9B6118ac2"
    ELK = "0xd8BaB53373B732Da40A7239359F141935dC00BfD"
    FEI = "0x956F47F50A910163D8BF957Cf5846D573E7f87CA"
    FLX = "0x6243d8CEA23066d098a15582d81a598b4e8391F4"
    GNO = "0x6810e776880C02933D47DB1b9fc05908e5386b96"
    ICHI = "0x903bEF1736CDdf2A537176cf3C64579C3867A881"
    IDLE = "0x875773784Af8135eA0ef43b5a374AaD105c5D39e"
    LDO = "0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32"
    LINK = "0x514910771AF9Ca656af840dff83E8264EcF986CA"
    MKR = "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2"
    NOTE = "0xCFEAead4947f0705A14ec42aC3D44129E1Ef3eD5"
    OHM = "0x64aa3364F17a4D01c6f1751Fd97C2BD3D7e7f1D5"
    osETH = "0xf1C9acDc66974dFB6dEcB12aA385b9cD01190E38"
    REP = "0x1985365e9f78359a9B6AD760e32412f4a445E862"
    rETH = "0xae78736Cd615f374D3085123A210448E74Fc6393"
    SAI = "0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359"
    sDAI = "0x83F20F44975D03b1b09e64809B757c47f942BEeA"
    sETH2 = "0xFe2e637202056d30016725477c5da089Ab0A043A"
    SNOTE = "0x38DE42F4BA8a35056b33A746A6b45bE9B1c3B9d2"
    spGNO = "0x7b481aCC9fDADDc9af2cBEA1Ff2342CB1733E50F"
    stETH = "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"
    stkAAVE = "0x4da27a545c0c5B758a6BA100e3a049001de870f5"
    STKAAVE = "0x4da27a545c0c5B758a6BA100e3a049001de870f5"
    stkABPT = "0xa1116930326D21fB917d5A27F1E9943A9595fb47"
    stkAURABAL = "0xfAA2eD111B4F580fCb85C48E6DC6782Dc5FCD7a6"
    SUSHI = "0x6B3595068778DD592e39A122f4f5a5cF09C90fE2"
    TUSD = "0x0000000000085d4780B73119b644AE5ecd22b376"
    UNI = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"
    unstETH = "0x889edC2eDab5f40e902b864aD4d7AdE8E412F9B1"
    USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    USDP = "0x8E870D67F660D95d5be530380D0eC0bd388289E1"
    USDT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    WBTC = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
    WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    weETH = "0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee"
    wstETH = "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0"
    X3CRV = "0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490"
    YFI = "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e"
    ZERO = "0x0000000000000000000000000000000000000000"
    ZRX = "0xE41d2489571d322189246DaFA5ebDe1F4699F498"


class GnosisTokenAddr:
    AGVE = "0x3a97704a1b25F08aa230ae53B352e2e72ef52843"
    AURA = "0x1509706a6c66CA549ff0cB464de88231DDBe213B"
    BAL = "0x7eF541E2a22058048904fE5744f9c7E4C57AF717"
    COW = "0x177127622c4A00F3d409B75571e12cB3c8973d3c"
    CRV = "0x712b3d230F3C1c19db860d80619288b1F0BDd0Bd"
    ELK = "0xE1C110E1B1b4A1deD0cAf3E42BfBdbB7b5d7cE1C"
    GNO = "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb"
    MAI = "0x3F56e0c36d275367b8C502090EDF38289b3dEa0d"
    nextDAI = "0x0e1D5Bcd2Ac5CF2f71841A9667afC1E995CaAf4F"
    nextUSDC = "0x44CF74238d840a5fEBB0eAa089D05b763B73faB8"
    nextUSDT = "0xF4d944883D6FddC56d3534986feF82105CaDbfA1"
    nextWETH = "0x538E2dDbfDf476D24cCb1477A518A82C9EA81326"
    osGNO = "0xF490c80aAE5f2616d3e3BDa2483E30C4CB21d1A0"
    STKAGAVE = "0x610525b415c1BFAeAB1a3fc3d85D87b92f048221"
    SYMM = "0xC45b3C1c24d5F54E7a2cF288ac668c74Dd507a84"
    USDC = "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83"
    USDT = "0x4ECaBa5870353805a9F068101A40E0f32ed605C6"
    WETH = "0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1"
    wstETH = "0x6C76971f98945AE98dD7d4DFcA8711ebea946eA6"
    WXDAI = "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d"
    x3CRV = "0x1337BedC9D22ecbe766dF105c9623922A27963EC"
    XGT = "0xC25AF3123d2420054c8fcd144c21113aa2853F39"
    DAI = "0x44fA8E6f47987339850636F88629646662444217"
    EURe = "0xcB444e90D8198415266c6a2724b7900fb12FC56E"
    GBPe = "0x5Cb9073902F2035222B9749F8fB0c9BFe5527108"


class PolygonTokenAddr:
    BAL = "0x9a71012B13CA4d3D0Cdc72A177DF3ef03b0E76A3"
    ELK = "0xeEeEEb57642040bE42185f49C52F7E9B38f8eeeE"
    MAI = "0xa3Fa99A148fA48D14Ed51d610c367C61876997F1"
    USDCe = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
    USDC = "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359"
    WETH = "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619"
    am3CRV = "0xE7a24EF0C5e95Ffb0f6684b813A78F2a3AD7D171"
    DAI = "0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063"


class ArbitrumTokenAddr:
    BAL = "0x040d1EdC9569d4Bab2D15287Dc5A4F10F56a56B8"
    DAI = "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1"
    weETH = "0x35751007a407ca6FEFfE80b3cB397736D2cf4dbe"


class BaseTokenAddr:
    weETH = "0x04C0599Ae5A44757c0af6F9eC3b93da8976c150A"


class EthereumContractSpecs:
    DAI = ContractSpec(address=EthereumTokenAddr.DAI, abi_path=current_dir() / "erc20.json", name="DAI")


# TODO: search for a better way, maybe remove EthereumTokenAddr
# for token in EthereumTokenAddr:
#    contract_spec = ContractSpec(address=token, abi_path=current_dir() / 'erc20.json', name=token.name)
#    setattr(EthereumContractSpecs, token.name, contract_spec)


Addresses = {
    Chain.ETHEREUM: EthereumTokenAddr,
    Chain.GNOSIS: GnosisTokenAddr,
    Chain.POLYGON: PolygonTokenAddr,
    Chain.ARBITRUM: ArbitrumTokenAddr,
    Chain.BASE: BaseTokenAddr,
}
