from defabipedia import Chain

from .helpers import get_config


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
    BSCSCAN = apikeys_cfg.get("bscscan", None)
    SNOWTRACE = apikeys_cfg.get("snowtrace", None)
    FTMSCAN = apikeys_cfg.get("ftmscan", None)
    OPTIMISTICETHERSCAN = apikeys_cfg.get("optimisticetherscan", None)
    ARBISCAN = apikeys_cfg.get("arbiscan", None)
    BASESCAN = apikeys_cfg.get("basescan", None)
    METISEXPLORER = apikeys_cfg.get("metisexplorer", None)
    ZAPPER = apikeys_cfg.get("zapper", None)
    ETHPLORER = apikeys_cfg.get("ethplorer", None)
    ROPSTEN = apikeys_cfg.get("etherscan", None)
    KOVAN = apikeys_cfg.get("etherscan", None)
    GOERLI = apikeys_cfg.get("etherscan", None)


class APIUrl(Constants):
    ETHERSCAN = "api.etherscan.io"
    POLSCAN = "api.polygonscan.com"
    GNOSISSCAN = "api.gnosisscan.io"
    BSCSCAN = "api.bscscan.com"
    SNOWTRACE = "api.snowtrace.io"
    FTMSCAN = "api.ftmscan.io"
    OPTIMISTICETHERSCAN = "api-optimistic.etherscan.io"
    ARBISCAN = "api.arbiscan.io"
    BASESCAN = "api.basescan.org/"
    METISEXPLORER = "api.routescan.io/v2/network/mainnet/evm/1088/etherscan/"
    ZAPPER = "api.zapper.fi"
    ETHPLORER = "api.ethplorer.io"
    ROPSTEN = "api-ropsten.etherscan.io"
    KOVAN = "api-kovan.etherscan.io"
    GOERLI = "api-goerli.etherscan.io"
