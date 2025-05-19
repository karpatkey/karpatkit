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
    ETHPLORER = apikeys_cfg.get("ethplorer", None)
    ROPSTEN = apikeys_cfg.get("etherscan", None)
    KOVAN = apikeys_cfg.get("etherscan", None)
    GOERLI = apikeys_cfg.get("etherscan", None)
    THEGRAPH = apikeys_cfg.get("thegraph", None)
    COINGECKO = apikeys_cfg.get("coingecko", None)


class APIUrl(Constants):
    ETHERSCAN = "https://api.etherscan.io/v2/api?chainid=1"
    POLSCAN = "https://api.etherscan.io/v2/api?chainid=137"
    GNOSISSCAN = "https://api.etherscan.io/v2/api?chainid=100"
    BSCSCAN = "https://api.etherscan.io/v2/api?chainid=8453" #pending?
    SNOWTRACE = "https://api.etherscan.io/v2/api?chainid=8453" #pending?
    FTMSCAN = "https://api.etherscan.io/v2/api?chainid=8453" #pending?
    OPTIMISTICETHERSCAN = "https://api.etherscan.io/v2/api?chainid=10"
    ARBISCAN = "https://api.etherscan.io/v2/api?chainid=42161"
    BASESCAN = "https://api.etherscan.io/v2/api?chainid=8453"
    METISEXPLORER = "https://api.etherscan.io/v2/api?chainid=" #pending?
    ZAPPER = "api.zapper.fi"
    ETHPLORER = "api.ethplorer.io"
    ROPSTEN = "api-ropsten.etherscan.io"
    KOVAN = "api-kovan.etherscan.io"
    GOERLI = "api-goerli.etherscan.io"


