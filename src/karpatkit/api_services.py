from .constants import Constants
from .helpers import get_config

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
    COINGECKO = apikeys_cfg.get("coingecko", None)
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
