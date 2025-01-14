import logging
import os
import warnings

import requests
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.providers import HTTPProvider, JSONBaseProvider

from defabipedia.types import Blockchain, Chain

from . import cache
from .helpers import get_config

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = float(os.environ.get("KKIT_NODE_TIMEOUT", 30))


def reset_providers():
    global _nodes_providers
    _nodes_providers = dict()


class AllProvidersDownError(Exception):
    pass


# store latest and archival ProviderManagers as they are used
_nodes_providers = dict()


class ProviderManager(JSONBaseProvider):
    def __init__(self, endpoints: list, max_fails_per_provider: int = 2, max_executions: int = 2):
        super().__init__()
        self.endpoints = endpoints
        self.max_fails_per_provider = max_fails_per_provider
        self.max_executions = max_executions
        self.providers = []

        for url in endpoints:
            if "://" not in url:
                logger.warning(f"Skipping invalid endpoint URI '{url}'.")
                continue
            provider = HTTPProvider(url, request_kwargs={"timeout": DEFAULT_TIMEOUT})
            errors = []
            self.providers.append((provider, errors))

    def make_request(self, method, params):
        for _ in range(self.max_executions):
            for provider, errors in self.providers:
                if len(errors) > self.max_fails_per_provider:
                    continue
                try:
                    response = provider.make_request(method, params)
                    return response
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 413:
                        raise ValueError(
                            {
                                "code": -32602,
                                "message": f"eth_getLogs and eth_newFilter are limited to {hex(10000)} blocks range",
                                "max_block_range": 10000,
                            }
                        ) from e  # Ad-hoc parsing: Quicknode nodes return a similar message
                except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
                    errors.append(e)
                    logger.error("Error when making request: %s", e)
                except Exception as e:
                    errors.append(e)
                    logger.exception("Unexpected exception when making request.")
            raise AllProvidersDownError(f"No working provider available. Endpoints {self.endpoints}")


def get_web3_provider(provider):
    web3 = Web3(provider)

    class CallCounterMiddleware:
        call_count = 0

        def __init__(self, make_request, w3):
            self.w3 = w3
            self.make_request = make_request

        @classmethod
        def increment(cls):
            cls.call_count += 1

        def __call__(self, method, params):
            self.increment()
            logger.debug("Web3 call count: %d", self.call_count)
            response = self.make_request(method, params)
            return response

    web3.middleware_onion.add(CallCounterMiddleware, "call_counter")
    if cache.is_enabled():
        # adding the cache after to get only effective calls counted by the counter
        web3.middleware_onion.add(cache.disk_cache_middleware, "disk_cache")
    return web3


def get_web3_call_count(web3):
    """Obtain the total number of calls that have been made by a web3 instance."""
    return web3.middleware_onion["call_counter"].call_count


def get_node(blockchain: Blockchain | str, block=None):
    """
    Return a node that does tries with multiple providers.

    The block parameter is not used and will be removed.
    """
    if block is not None:
        warnings.warn("get_node() block argument is deprecated. Just remove it.", DeprecationWarning, stacklevel=2)

    node_endpoints = get_config()["nodes"]
    if blockchain not in node_endpoints:
        raise ValueError(f"Unknown blockchain '{blockchain}'")
    endpoints = node_endpoints[blockchain]
    if isinstance(endpoints, dict):
        warnings.warn(
            "endpoint config latest and archival is deprecated. Use a list instead.", DeprecationWarning, stacklevel=2
        )
        endpoints = endpoints["latest"] + endpoints["archival"]
    if not endpoints:
        raise ValueError(f"No configured nodes for blockchain {blockchain}")

    providers = _nodes_providers.get(blockchain, None)
    if not providers:
        providers = ProviderManager(endpoints=endpoints)
        _nodes_providers[blockchain] = providers

    web3 = get_web3_provider(providers)
    web3._network_name = str(blockchain)  # TODO: remove this. Use Chains.get_blockchain_from_web3()

    if blockchain == Chain.AVALANCHE:
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        # https://web3py.readthedocs.io/en/stable/middleware.html#proof-of-authority
    return web3
