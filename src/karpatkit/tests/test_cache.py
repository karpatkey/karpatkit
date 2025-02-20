from unittest import mock

import diskcache
import pytest

from karpatkit.cache import (
    cache_call,
    cache_contract_method,
    const_call,
    del_key,
    disk_cache_middleware,
    get_value,
    set_value,
)


@pytest.fixture
def temporary_cache(monkeypatch):
    monkeypatch.setattr("karpatkit.cache._cache", diskcache.Cache())


@pytest.fixture
def disable_cache(monkeypatch):
    monkeypatch.setattr("karpatkit.cache._cache", None)


def test_get_set_in(temporary_cache):
    set_value("foo", "bar")
    assert get_value("foo") == "bar"
    del_key("foo")
    with pytest.raises(KeyError):
        get_value("foo")


def build_web3_contract_mock():
    centinel = mock.Mock()
    web3_contract_function = mock.Mock()
    web3_contract_function.address = "0xcafe"
    web3_contract_function.args = tuple()
    web3_contract_function.kwargs = dict()
    web3_contract_function.function_identifier = "decimals"
    web3_contract_function.w3._network_name = "ethereum"

    def _call():
        centinel()

    web3_contract_function.call = _call
    return web3_contract_function, centinel


def test_cache_decorator(temporary_cache):
    centinel = mock.Mock()

    @cache_call(exclude_args=["c", "d"])
    def f(a, b, c, d=None):
        centinel()
        return a + b + c

    assert f(1, 2, 0) == 3
    assert centinel.call_count == 1
    assert f(1, 2, 0) == 3
    assert f(1, 2, 0, "foo") == 3
    assert f(1, 2, 3, d="foo") == 3
    assert centinel.call_count == 1  # only called once


def test_const_call(temporary_cache):
    web3_contract_function, centinel = build_web3_contract_mock()
    const_call(web3_contract_function)
    assert centinel.call_count == 1
    const_call(web3_contract_function)
    assert centinel.call_count == 1  # only called once


def test_const_cache_disabled():
    web3_contract_function, centinel = build_web3_contract_mock()
    with mock.patch("karpatkit.cache.is_enabled", wraps=lambda: False):
        const_call(web3_contract_function)
        const_call(web3_contract_function)
        assert centinel.call_count == 2


def test_cache_contract_method_when_disable_cache(disable_cache):
    class Contract:
        @cache_contract_method()
        def method(self):
            pass

        class contract:
            address = "0x1234567890abcdf"

    contract = Contract()
    contract.method()


def test_cache_middleware_when_disable_cache(disable_cache):
    web3 = mock.Mock()
    web3._network_name = "network_name"
    middleware = disk_cache_middleware(mock.Mock(), web3)
    middleware("eth_chainId", params={})
