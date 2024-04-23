from contextlib import suppress

import pytest

from defabipedia import Chain
from karpatkit import nodetime
from karpatkit.nodetime import blocks_around_time, create_blocks_time_dict, parallel_blocks_around_time

latest = dict(
    [
        (Chain.ETHEREUM, {"number": 19_693_336, "timestamp": 1_713_576_335}),
        (Chain.AVALANCHE, {"number": 44_421_503, "timestamp": 1_713_576_337}),
        (Chain.FANTOM, {"number": 79_676_149, "timestamp": 1_713_576_336}),
        (Chain.GNOSIS, {"number": 33_531_685, "timestamp": 1_713_576_325}),
        (Chain.ARBITRUM, {"number": 202_813_437, "timestamp": 1_713_576_341}),
        (Chain.OPTIMISM, {"number": 118_988_778, "timestamp": 1_713_576_333}),
        (Chain.BASE, {"number": 13_393_498, "timestamp": 1_713_576_343}),
    ]
)

msgs = set()


def test_latest():
    a, c = "{ }".split()
    for chain in Chain.all():
        if chain in latest:
            continue
        try:
            block = nodetime.get_node(chain).eth.get_block("latest")
        except Exception:
            pass
        else:
            print(f'\n({chain}, {a}"number": {block.number}, "timestamp": {block.timestamp}{c}),')


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


ts = 1_713_576_335

expected_simple_dict = {
    Chain.ETHEREUM: 19_693_336,
    Chain.AVALANCHE: 44_421_502,
    Chain.FANTOM: 79_676_148,
    Chain.GNOSIS: 33_531_686,
    Chain.ARBITRUM: pytest.approx(202_813_415, abs=4),
    Chain.BASE: 13_393_494,
}


@pytest.mark.asyncio
async def test_parallel_blocks_around_time():
    blocks_dict = await parallel_blocks_around_time(timestamp=ts)
    print()
    for chain, result in blocks_dict.items():
        if isinstance(result, Exception):
            print(chain, type(result))
        else:
            left, right = result
            print(chain, left.number, right.number, left.timestamp - ts, right.timestamp - ts)

    print("\nException skipped")
    tolerance_s = 60
    for chain, (left, right) in blocks_dict.drop_exceptions().items():
        print(chain, left.number, right.number, left.timestamp - ts, right.timestamp - ts)

        assert -tolerance_s <= (left.timestamp - ts) <= 0
        assert 0 <= (right.timestamp - ts) <= tolerance_s

        assert 0 <= (right.number - left.number) <= 1

    simple_dict = blocks_dict.drop_exceptions().simple
    for chain in expected_simple_dict:
        with suppress(KeyError):
            assert simple_dict[chain] == expected_simple_dict[chain]


def test_create_blocks_time_dict():
    simple_dict = create_blocks_time_dict(ts)
    for chain in expected_simple_dict:
        with suppress(KeyError):
            assert simple_dict[chain] == expected_simple_dict[chain]


def test_create_blocks_time_dict_latest():
    simple_dict = create_blocks_time_dict()
    for chain in expected_simple_dict:
        if chain == Chain.ARBITRUM:
            continue
        with suppress(KeyError):
            assert simple_dict[chain] > expected_simple_dict[chain]
