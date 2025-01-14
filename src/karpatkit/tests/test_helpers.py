from unittest.mock import Mock

import pytest
from web3.exceptions import BadFunctionCallOutput, ContractLogicError

from karpatkit import helpers


@pytest.mark.parametrize("code", helpers.suppressed_error_codes)
def test_suppress_error_codes(code):
    with helpers.suppress_error_codes():
        raise ValueError({"code": code})


@pytest.fixture
def not_suppressed_code():
    code = -30_000
    assert code not in helpers.suppressed_error_codes
    return code


def test_not_suppress_error_codes(not_suppressed_code):
    with pytest.raises(ValueError), helpers.suppress_error_codes():
        raise ValueError({"code": not_suppressed_code})


def test_call_contract_method():
    method = Mock()
    method.call = Mock(return_value=1)
    block = 3
    ret_value = helpers.call_contract_method(method, block)
    assert ret_value == 1
    method.call.assert_called_with(block_identifier=block)


@pytest.mark.parametrize(
    "exception",
    [
        BadFunctionCallOutput,
        ContractLogicError,
        *(ValueError({"code": code}) for code in helpers.suppressed_error_codes),
    ],
)
def test_call_contract_method_suppress(exception):
    method = Mock()
    method.call = Mock(side_effect=exception)
    block = 3
    ret_value = helpers.call_contract_method(method, block)
    assert ret_value is None
    method.call.assert_called_with(block_identifier=block)


def test_call_contract_method_raise(not_suppressed_code):
    method = Mock()
    method.call = Mock(side_effect=ValueError({"code": not_suppressed_code}))
    block = 3
    with pytest.raises(ValueError):
        helpers.call_contract_method(method, block)
    method.call.assert_called_with(block_identifier=block)


def test_listify():
    @helpers.listify
    def seq():
        yield 1
        yield 2

    ret_value = seq()
    assert isinstance(ret_value, list)
    assert ret_value == [1, 2]


def test_suppress_value():
    with helpers.suppress_value(ValueError, "something"):
        raise ValueError("something")


@pytest.mark.parametrize(
    "exception",
    [
        ValueError("different"),
        ValueError(),
        ValueError,
        TypeError,
    ],
)
def test_suppress_value_doesnt_match(exception):
    with pytest.raises(Exception), helpers.suppress_value(ValueError, "something"):  # noqa: B017
        raise exception
