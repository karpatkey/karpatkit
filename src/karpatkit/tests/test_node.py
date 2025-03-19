import pytest
import requests

from karpatkit import Chain, cache, node


@pytest.fixture
def nocache(monkeypatch):
    monkeypatch.setattr(cache, "_cache", None)


def test_change_timeout(monkeypatch, nocache):
    monkeypatch.setattr(node, "DEFAULT_TIMEOUT", 0.1)
    monkeypatch.setattr(requests.sessions.Session, "request", deny_network)
    w3 = node.get_node(Chain.ETHEREUM)
    with pytest.raises(node.AllProvidersDownError):
        w3.eth.get_block(1)


def deny_network(*args, **kwargs):
    raise RuntimeError("Simulate non-reachable")


def test_max_length(monkeypatch, nocache):
    monkeypatch.setattr(node, "DEFAULT_MAX_LENGTH", 1)
    w3 = node.get_node(Chain.GNOSIS)
    with pytest.raises(node.MaxLengthError):
        w3.eth.get_block(1)
