import pytest

from defabipedia import Chain
from karpatkit import nodetime
from karpatkit.nodetime import blocks_around_time

latest = dict(
    [
        (Chain.ETHEREUM, {"number": 19693336, "timestamp": 1713576335}),
        (Chain.AVALANCHE, {"number": 44421503, "timestamp": 1713576337}),
        (Chain.FANTOM, {"number": 79676149, "timestamp": 1713576336}),
        (Chain.GNOSIS, {"number": 33531685, "timestamp": 1713576325}),
        (Chain.ARBITRUM, {"number": 202813437, "timestamp": 1713576341}),
        (Chain.OPTIMISM, {"number": 118988778, "timestamp": 1713576333}),
        (Chain.BASE, {"number": 13393498, "timestamp": 1713576343}),
    ]
)

msgs = set()


def test_latest():
    a, c = "{ }".split()
    for name, chain in Chain._by_name.items():
        if chain in latest:
            continue
        try:
            block = nodetime.get_node(chain).eth.get_block("latest")
        except Exception:
            pass
        else:
            print(f'\n({name}, {a}"number": {block.number}, "timestamp": {block.timestamp}{c}),')


@pytest.fixture(params=Chain._by_name.values())
def blockchain(request):
    chain = request.param
    try:
        nodetime.get_node(chain).eth.get_block(1)
    except Exception as e:
        msg = str(e)
        if msg not in msgs:
            msgs.add(msg)
            pytest.skip(f"{hash(msg)}: {msg}")
        else:
            pytest.skip(f"{hash(msg)}: Idem")

    else:
        return chain


@pytest.fixture(params="genesis early middle late".split())
def timestamp(blockchain, request, block_latest):
    node = nodetime.get_node(blockchain)
    match request.param:
        case "genesis":
            return node.eth.get_block(1).timestamp
        case "early":
            return node.eth.get_block(1).timestamp + 3600
        case "middle":
            return (node.eth.get_block(1).timestamp + block_latest.timestamp) / 2
        case "late":
            return block_latest.timestamp - 3600


@pytest.fixture
def block_latest(blockchain):
    node = nodetime.get_node(blockchain)
    block = node.eth.get_block("latest")
    try:
        fixed_latest = latest[blockchain]
    except KeyError:
        pass
    else:
        block.__dict__.update(fixed_latest)
    return block


@pytest.fixture(params="pregenesis postlatest".split())
def outside_timestamp(blockchain, request, block_latest):
    node = nodetime.get_node(blockchain)
    match request.param:
        case "pregenesis":
            return node.eth.get_block(1).timestamp - 3600
        case "latest":
            return block_latest.timestamp
        case "postlatest":
            return block_latest.timestamp + 3600


def test_blocks_around_time_ok(blockchain, timestamp, block_latest):
    left_block, right_block = blocks_around_time(blockchain, timestamp, n_max=block_latest.number - 1)
    assert (right_block.number - left_block.number) in {0, 1}
    assert left_block.timestamp <= timestamp
    assert right_block.timestamp >= timestamp


def test_blocks_around_time_outside(blockchain, outside_timestamp, block_latest):
    with pytest.raises(IndexError):
        blocks_around_time(blockchain, outside_timestamp, n_max=block_latest.number - 1)
