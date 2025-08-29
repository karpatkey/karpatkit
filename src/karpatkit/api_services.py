from .constants import Constants
from .helpers import get_config

apikeys_cfg = get_config()["apikeys"]


class APIKey(Constants):
    ETHERSCAN = apikeys_cfg.get("etherscan", None)
    POLSCAN = apikeys_cfg.get("etherscan", None)
    GNOSISSCAN = apikeys_cfg.get("etherscan", None)
    BSCSCAN = apikeys_cfg.get("etherscan", None)
    SNOWTRACE = apikeys_cfg.get("snowtrace", None)
    FTMSCAN = apikeys_cfg.get("etherscan", None)
    OPTIMISTICETHERSCAN = apikeys_cfg.get("etherscan", None)
    ARBISCAN = apikeys_cfg.get("etherscan", None)
    BASESCAN = apikeys_cfg.get("etherscan", None)
    LINEASCAN = apikeys_cfg.get("etherscan", None)
    METISEXPLORER = apikeys_cfg.get("metisexplorer", None)
    ZAPPER = apikeys_cfg.get("zapper", None)
    ETHPLORER = apikeys_cfg.get("ethplorer", None)
    ROPSTEN = apikeys_cfg.get("etherscan", None)
    KOVAN = apikeys_cfg.get("etherscan", None)
    GOERLI = apikeys_cfg.get("etherscan", None)
    THEGRAPH = apikeys_cfg.get("thegraph", None)
    COINGECKO = apikeys_cfg.get("coingecko", None)


class APIUrl(Constants):
    # using etherscan api v2 with chain id parameter.
    ETHERSCAN = "api.etherscan.io/v2/api?chainid=1"
    POLSCAN = "api.etherscan.io/v2/api?chainid=137"
    GNOSISSCAN = "api.etherscan.io/v2/api?chainid=100"
    BSCSCAN = "api.etherscan.io/v2/api?chainid=56"
    SNOWTRACE = "api.snowtrace.io"
    FTMSCAN = "api.etherscan.io/v2/api?chainid=250"
    OPTIMISTICETHERSCAN = "api.etherscan.io/v2/api?chainid=10"
    ARBISCAN = "api.etherscan.io/v2/api?chainid=42161"
    BASESCAN = "api.etherscan.io/v2/api?chainid=8453"
    LINEASCAN = "api.etherscan.build/v2/api?chainid=59144"
    METISEXPLORER = "api.routescan.io/v2/network/mainnet/evm/1088/etherscan/api"
    ZAPPER = "api.zapper.fi/api"
    ETHPLORER = "api.ethplorer.io/api"
    ROPSTEN = "api-ropsten.etherscan.io/api"
    KOVAN = "api-kovan.etherscan.io/api"
    GOERLI = "api-goerli.etherscan.io/api"
