import json
import os
from contextlib import contextmanager, suppress
from functools import wraps
from typing import Any

from web3.exceptions import BadFunctionCallOutput, ContractLogicError

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
