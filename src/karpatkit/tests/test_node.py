from karpatkit import Chain, node


def test_change_timeout(monkeypatch):
    monkeypatch.setattr(node, "DEFAULT_TIMEOUT", 7)
    monkeypatch.setattr(node, "_nodes_providers", {})
    node.reset_providers()
    w3 = node.get_node(Chain.ETHEREUM)
    w3.eth.get_block(1)
    assert w3.provider.providers[0][0].get_request_kwargs()["timeout"] == 7
