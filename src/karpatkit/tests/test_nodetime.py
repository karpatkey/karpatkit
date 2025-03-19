import pytest

from defabipedia import Chain
from karpatkit import nodetime
from karpatkit.nodetime import Block

now = 1_715_191_991
requested_time = 1_713_576_344

expected_block_for = {
    Chain.ETHEREUM: Block(number=19_693_336, timestamp=1_713_576_335),
    Chain.AVALANCHE: Block(number=44_421_506, timestamp=1_713_576_343),
    Chain.FANTOM: Block(number=79_676_154, timestamp=1_713_576_343),
    Chain.GNOSIS: Block(number=33_531_687, timestamp=1_713_576_340),
    Chain.ARBITRUM: Block(number=202_813_448, timestamp=1_713_576_344),
    Chain.OPTIMISM: Block(number=118_988_778, timestamp=1_713_576_333),
    Chain.BASE: Block(number=13_393_498, timestamp=1_713_576_343),
}

latest_block_numbers = {
    Chain.ETHEREUM: 19_827_051,
    Chain.AVALANCHE: 45_192_061,
    Chain.FANTOM: 80_620_273,
    Chain.GNOSIS: 33_844_062,
    Chain.ARBITRUM: 209_205_524,
    Chain.OPTIMISM: 119_796_916,
    Chain.BASE: 14_201_635,
}


original_get_latest_block_number = nodetime.get_latest_block_number


def mocked_get_latest_block_number(blockchain):
    try:
        block_number = latest_block_numbers[blockchain]
    except KeyError:
        block_number = latest_block_numbers[blockchain] = original_get_latest_block_number(blockchain)
    return block_number


@pytest.fixture(autouse=True)
def fixed_latest(monkeypatch):
    monkeypatch.setattr(nodetime, "get_latest_block_number", mocked_get_latest_block_number)


def test_all_chains_block_before_time():
    r = nodetime.all_chains_block_before_time(requested_time)
    available_chains = set(expected_block_for).intersection(r)
    assert len(available_chains) > 0
    for chain in available_chains:
        if chain in {Chain.ARBITRUM}:
            assert r[chain].timestamp == expected_block_for[chain].timestamp
            assert abs(r[chain].timestamp - expected_block_for[chain].timestamp) <= 4
            # because some consecutive blocks have the same timestamp
        else:
            assert r[chain] == expected_block_for[chain]


def test_all_chains_block_before_time_latest():
    last_7_minutes = now - 7 * 60
    r = nodetime.all_chains_block_before_time()
    available_chains = set(expected_block_for).intersection(r)
    assert len(available_chains) > 0
    for chain in available_chains:
        assert r[chain].number > expected_block_for[chain].number
        assert r[chain].timestamp > last_7_minutes


@pytest.mark.asyncio
async def test_async_all_chains_get_latest_block():
    r = await nodetime.async_all_chains_get_latest_block()
    for chain in expected_block_for:
        assert isinstance(r[chain], Block | Exception)


@pytest.mark.asyncio
async def test_async_all_chains_block_before_time():
    r = await nodetime.async_all_chains_block_before_time(requested_time)
    for chain in expected_block_for:
        assert isinstance(r[chain], Block | Exception)


## Individual tests

msgs = set()


@pytest.fixture(params=Chain.all())
def blockchain(request):
    chain = request.param
    try:
        nodetime.get_block(chain, 1)
    except Exception as e:
        msg = str(e)
        if msg not in msgs:
            msgs.add(msg)
            pytest.skip(f"{hash(msg)}: {msg}")
        else:
            pytest.skip(f"{hash(msg)}: Idem")

    else:
        return chain


@pytest.fixture
def latest_block(blockchain):
    return nodetime.get_latest_block(blockchain)


@pytest.fixture(params="genesis early middle late".split())
def timestamp(blockchain, request, latest_block):
    match request.param:
        case "genesis":
            return nodetime.get_block(blockchain, 1).timestamp
        case "early":
            return nodetime.get_block(blockchain, 1).timestamp + 3600
        case "middle":
            return (nodetime.get_block(blockchain, 1).timestamp + latest_block.timestamp) / 2
        case "late":
            return latest_block.timestamp - 3600


@pytest.fixture(params="pregenesis postlatest".split())
def outside_timestamp(blockchain, request, latest_block):
    match request.param:
        case "pregenesis":
            return nodetime.get_block(blockchain, 1).timestamp - 3600
        case "postlatest":
            return latest_block.timestamp + 3600


def test_blocks_around_time_ok(blockchain, timestamp):
    block_before, block_after = nodetime.blocks_around_time(blockchain, timestamp)
    assert (block_after.number - block_before.number) in {0, 1}
    assert block_before.timestamp <= timestamp
    assert block_after.timestamp >= timestamp


def test_blocks_before_time_ok(blockchain):
    block = nodetime.block_before_time(blockchain, requested_time)
    if blockchain in [Chain.ARBITRUM]:
        assert block.timestamp == expected_block_for[blockchain].timestamp
        assert abs(block.timestamp - expected_block_for[blockchain].timestamp) <= 4
        # because some consecutive blocks have the same timestamp
    else:
        assert block == expected_block_for[blockchain]


def test_blocks_around_time_outside(blockchain, outside_timestamp):
    with pytest.raises(IndexError):
        nodetime.blocks_around_time(blockchain, outside_timestamp)
