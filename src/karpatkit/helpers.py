import json
import os
from contextlib import contextmanager, suppress
from functools import wraps
from typing import Any

from web3.exceptions import BadFunctionCallOutput, ContractLogicError

from defabipedia.tokens import erc20_contract, NATIVE, EthereumTokenAddr

suppressed_error_codes = {-32000, -32015}


class ConfigError(Exception):
    pass


def get_config():
    config_path = os.environ.get("KKIT_CFG") or os.environ.get("CONFIG_PATH") or "kkit_config.json"

    if config_path and os.path.exists(config_path):
        with open(config_path) as json_file:
            config = json.load(json_file)
    else:
        raise ConfigError("Config file is missing. Use KKIT_CFG env variable to specify a config file.")
    return config


@contextmanager
def suppress_error_codes():
    try:
        yield
    except ValueError as e:
        if e.args[0]["code"] not in suppressed_error_codes:
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
