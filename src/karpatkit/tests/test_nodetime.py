from unittest.mock import Mock

import pytest
from web3.exceptions import BlockNotFound

from defabipedia import Chain
from karpatkit import nodetime
from karpatkit.nodetime import blocks_around_time


@pytest.fixture(params=Chain._by_name.values())
def blockchain(request):  # , mock_node):
    chain = request.param
    try:
        nodetime.get_node(chain).eth.get_block(1)
    except Exception as e:
        pytest.skip(str(e))
    else:
        return chain


# @pytest.fixture(params="genesis early middle late latest".split())
@pytest.fixture(params="genesis early middle late".split())
def timestamp(blockchain, request):
    node = nodetime.get_node(blockchain)
    match request.param:
        case "genesis":
            return node.eth.get_block(1).timestamp
        case "early":
            return node.eth.get_block(1).timestamp + 3600
        case "middle":
            return (node.eth.get_block(1).timestamp + node.eth.get_block("latest").timestamp) / 2
        case "late":
            return node.eth.get_block("latest").timestamp - 3600


@pytest.fixture(params="pregenesis postlatest".split())
def outside_timestamp(blockchain, request):
    node = nodetime.get_node(blockchain)
    match request.param:
        case "pregenesis":
            return node.eth.get_block(1).timestamp - 3600
        case "latest":
            return node.eth.get_block("latest").timestamp
        case "postlatest":
            return node.eth.get_block("latest").timestamp + 3600


def test_blocks_around_time(blockchain, timestamp):
    left_block, right_block = blocks_around_time(blockchain, timestamp)
    assert (right_block.number - left_block.number) in {0, 1}


def test_blocks_around_time_outside(blockchain, outside_timestamp):
    with pytest.raises(IndexError):
        blocks_around_time(blockchain, outside_timestamp)


@pytest.fixture
def mock_node(monkeypatch):
    min_number = 0
    max_number = 19_691_386

    def get_block(block_identifier):
        if block_identifier == "latest":
            _number = max_number
        else:
            _number = block_identifier
            if block_identifier < min_number:
                raise ValueError
            if block_identifier > max_number:
                raise BlockNotFound

        class block:
            number = int(_number)
            timestamp = 1_438_269_988.0 + _number**1.01 * 12.0

        return block

    node = Mock()
    node.eth.get_block = get_block
    monkeypatch.setattr(nodetime, "get_node", Mock(return_value=node))
    monkeypatch.setattr(nodetime, "max_iterations", 1000)
    return node
