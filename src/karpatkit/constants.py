from .helpers import get_config
from defabipedia import Chain


class ConstantsMeta(type):
    def __setattr__(cls, name, value):
        raise AttributeError("Read only")


class Constants(metaclass=ConstantsMeta):
    pass


TESTNET_CHAINS = [Chain.ROPSTEN, Chain.KOVAN, Chain.GOERLI]

# ERC-20, GENERAL, ABI Token Simplified - name, symbol, SYMBOL, decimals, balanceOf, totalSupply
ABI_TOKEN_SIMPLIFIED = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}, {"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"}, {"constant":true,"inputs":[],"name":"SYMBOL","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}, {"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"}, {"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}, {"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'


class Address(Constants):
    ZERO = "0x0000000000000000000000000000000000000000"
    E = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"


apikeys_cfg = get_config()["apikeys"]


class APIKey(Constants):
    ETHERSCAN = apikeys_cfg.get("etherscan", None)
    POLSCAN = apikeys_cfg.get("polscan", None)
    GNOSISSCAN = apikeys_cfg.get("gnosisscan", None)
    BINANCE = apikeys_cfg.get("binance", None)
    AVALANCHE = apikeys_cfg.get("avalanche", None)
    FANTOM = apikeys_cfg.get("fantom", None)
    OPTIMISM = apikeys_cfg.get("optimism", None)
    ARBITRUM = apikeys_cfg.get("arbitrum", None)
    ZAPPER = apikeys_cfg.get("zapper", None)
    ETHPLORER = apikeys_cfg.get("ethplorer", None)
    ROPSTEN = apikeys_cfg.get("etherscan", None)
    KOVAN = apikeys_cfg.get("etherscan", None)
    GOERLI = apikeys_cfg.get("etherscan", None)


class APIUrl(Constants):
    ETHERSCAN = "api.etherscan.io"
    POLSCAN = "api.polygonscan.com"
    GNOSISSCAN = "api.gnosisscan.io"
    BINANCE = "api.bscscan.com"
    AVALANCHE = "api.snowtrace.io"
    FANTOM = "api.ftmscan.io"
    OPTIMISM = "api-optimistic.etherscan.io"
    ARBITRUM = "api.arbiscan.io"
    ZAPPER = "api.zapper.fi"
    ETHPLORER = "api.ethplorer.io"
    ROPSTEN = "api-ropsten.etherscan.io"
    KOVAN = "api-kovan.etherscan.io"
    GOERLI = "api-goerli.etherscan.io"
