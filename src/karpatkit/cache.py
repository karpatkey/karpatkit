import functools
import logging
import os
from inspect import getcallargs

import diskcache
from web3._utils.caching.caching_utils import generate_cache_key

from .helpers import suppressed_error_codes

logger = logging.getLogger(__name__)

VERSION = 7
VERSION_CACHE_KEY = "VERSION"

_cache = None


def check_version():
    version = _cache.get(VERSION_CACHE_KEY, 0)
    if version != VERSION:
        _cache.clear()
        _cache[VERSION_CACHE_KEY] = VERSION
        logger.info(f"Old cache version! Creating new cache with version: {VERSION}")


if not os.environ.get("KKIT_CACHE_DISABLE"):
    cache_dir = os.environ.get("KKIT_CACHE_DIR", "/tmp/kkit/")
    logger.debug(f"Cache enabled. Storage is at '{cache_dir}'.")

    # If a value serialized size is great than disk_min_file_size then it will be
    # saved into a file and not into the sqlite cache.db
    MIN_FILE_SIZE_BYTES = 250 * 1024 * 1024
    _cache = diskcache.Cache(directory=cache_dir, disk_min_file_size=MIN_FILE_SIZE_BYTES)
    check_version()
    if os.environ.get("KKIT_CACHE_CLEAR"):
        _cache.clear()
else:
    logger.debug("Cache is disabled")


def is_enabled():
    return _cache is not None


def clear():
    if is_enabled():
        _cache.clear()


def get_value(key):
    """Get a value from the cache.

    Returns:
        The cached value.

    Raises:
        KeyError: The key doesn't exist in the cache or there is no value associated with that key.
    """
    return _cache[key]


def set_value(key, value):
    """Set a value to the cache"""
    _cache[key] = value


def del_key(key):
    """Delete a key from the cache"""
    del _cache[key]


def disk_cache_middleware(make_request, web3):
    """
    Cache middleware that supports multiple blockchains.
    It also do not caches if block='latest'.
    """

    RPC_WHITELIST = {
        "eth_chainId",
        "eth_call",
        "eth_getTransactionReceipt",
        "eth_getLogs",
        "eth_getTransactionByHash",
        "eth_getCode",
        "eth_getStorageAt",
        "eth_getBlockByNumber",
        "debug_traceTransaction",
        "trace_transaction",
    }

    def middleware(method, params):
        if not is_enabled():
            logger.debug("The cache is disabled")
            return make_request(method, params)

        do_cache = False
        if method in RPC_WHITELIST and "latest" not in params:
            do_cache = True
        if method in {"eth_chainId", "eth_getCode"}:
            do_cache = True

        if do_cache:
            params_hash = generate_cache_key(params)
            cache_key = f"{web3._network_name}.{method}.{params_hash}"
            try:
                key, data = get_value(cache_key)
            except KeyError:
                response = make_request(method, params)
                if "error" not in response and "result" in response and response["result"] is not None:
                    set_value(cache_key, ("result", response["result"]))
                elif "error" in response:
                    if response["error"]["code"] in suppressed_error_codes:
                        set_value(cache_key, ("error", response["error"]))
                return response
            else:
                return {"jsonrpc": "2.0", "id": 11, key: data}
        else:
            logger.debug(f"Not caching '{method}' with params: '{params}'")
            return make_request(method, params)

    return middleware


def cache_contract_method(exclude_args=None, validator=None):
    def decorator(f):
        @functools.wraps(f)
        def method_wrapper(*args, **kwargs):
            if not is_enabled():
                logger.debug("The cache is disabled")
                return f(*args, **kwargs)

            cache_args = getcallargs(f, *args, **kwargs)
            obj = cache_args.pop("self")
            if exclude_args:
                for arg in exclude_args:
                    cache_args.pop(arg)
            cache_key = generate_cache_key((obj.contract.address, f.__qualname__, cache_args))

            def refreshed_result():
                result = f(*args, **kwargs)
                set_value(cache_key, result)
                return result

            if validator is None:
                return refreshed_result()

            try:
                cached_result = get_value(cache_key)
            except KeyError:
                return refreshed_result()

            if validator(obj, **cached_result):
                return cached_result
            else:
                return refreshed_result()

        return method_wrapper

    return decorator


def cache_call(exclude_args=None, filter=None, is_method=False, include_attrs=None):
    """Decorator to cache the result of a function.

    It has the ability to exclude arguments that the result
    of the call is not dependant.

    In the following example, the function does not depend on the http_client:

    @cache_call(exclude_args=['http_client'])
    def get_pi_digits(http_client, count):
        response = http_client.get(f"https://api.pi.delivery/v1/pi?start=0&numberOfDigits={count}")
        return response["content"]

    A filter function can be provided to add conditions, based on arguments, to cache the result.
    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if not is_enabled():
                logger.debug("The cache is disabled")
                return f(*args, **kwargs)
            all_args = getcallargs(f, *args, **kwargs)
            cache_args = all_args.copy()
            if is_method:
                obj = cache_args.pop("self")
            if filter is None or filter(cache_args):
                if exclude_args:
                    for arg in exclude_args:
                        cache_args.pop(arg)

                if is_method:
                    key_tuple = obj.__class__.__name__, f.__qualname__, cache_args
                elif include_attrs:
                    obj = all_args["self"]
                    attrs_value = [getter(obj) for getter in include_attrs]
                    key_tuple = tuple(attrs_value + [f.__qualname__, cache_args])
                else:
                    key_tuple = f.__qualname__, cache_args

                cache_key = generate_cache_key(key_tuple)

                try:
                    result = get_value(cache_key)
                except KeyError:
                    result = f(*args, **kwargs)
                    set_value(cache_key, result)
            else:
                result = f(*args, **kwargs)
            return result

        return wrapper

    return decorator


def const_call(f):
    """Utility to do .call() on web3 contracts that are known to be cacheable"""
    if not is_enabled():
        return f.call()

    cache_key = generate_cache_key((f.w3._network_name, f.address, f.function_identifier, f.args, f.kwargs))
    try:
        return get_value(cache_key)
    except KeyError:
        result = f.call()
        set_value(cache_key, result)
        return result
