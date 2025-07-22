import json
import os
from contextlib import contextmanager, suppress
from functools import wraps
from typing import Any

from web3.exceptions import BadFunctionCallOutput, ContractLogicError, Web3RPCError

from defabipedia.tokens import NATIVE, EthereumTokenAddr, erc20_contract

suppressed_error_codes = {-32000, -32015}


class ConfigError(Exception):
    pass


_CONFIG = None


def get_config():
    global _CONFIG
    config_path = os.environ.get("KKIT_CFG") or os.environ.get("CONFIG_PATH") or "kkit_config.json"

    if _CONFIG:
        return _CONFIG

    json_config = os.environ.get("KKIT_CFG_JSON")
    if json_config:
        _CONFIG = json.loads(json_config)
        return _CONFIG

    if config_path and os.path.exists(config_path):
        with open(config_path) as json_file:
            _CONFIG = json.load(json_file)
    else:
        raise ConfigError("Config file is missing. Use KKIT_CFG env variable to specify a config file.")
    return _CONFIG


@contextmanager
def suppress_error_codes():
    try:
        yield
    except Web3RPCError as e:
        if isinstance(e.args[0], dict) and e.args[0].get("code", 0) not in suppressed_error_codes:
            raise
    except ValueError as e:
        if isinstance(e.args[0], dict) and e.args[0].get("code", 0) not in suppressed_error_codes:
            raise


@contextmanager
def suppress_value(exception, value):
    try:
        yield
    except exception as e:
        if e.args[0] != value:
            raise


def call_contract_method(method, block) -> Any | None:
    with suppress(ContractLogicError, BadFunctionCallOutput), suppress_error_codes():
        return method.call(block_identifier=block)


def listify(func):
    """
    Decorator to cast the returned iterable into a list.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return list(func(*args, **kwargs))

    return wrapper


def get_balance(w3, token, address):
    """Get the token or ETH balance of an address"""
    if token == NATIVE or token == EthereumTokenAddr.ZERO:  # Check allso with ZERO to maintain backwards compat
        return w3.eth.get_balance(address)
    else:
        ctract = erc20_contract(w3, token)
        return ctract.functions.balanceOf(address).call()


def get_allowance(w3, token, owner_address, spender_address):
    """Get the token allowance of an address"""
    ctract = erc20_contract(w3, token)
    return ctract.functions.allowance(owner_address, spender_address).call()
