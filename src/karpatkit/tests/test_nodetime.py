from karpatkit.nodetime import blocks_around_time
from defabipedia import Chain
import pytest

@pytest.mark.parametrize("timestamp", [1_713_472_493, 1_538_269_000, 1_600_000_000])
def test_blocks_around_time(timestamp):
    left_block, right_block = blocks_around_time(Chain.ETHEREUM, timestamp)
    print(left_block.number, right_block.number, right_block.number - left_block.number,
    left_block.timestamp, right_block.timestamp, right_block.timestamp - left_block.timestamp)
    assert (right_block.number - left_block.number) in {0, 1}
    assert abs(timestamp - left_block.timestamp) <= 12
    assert abs(timestamp - right_block.timestamp) <= 12
