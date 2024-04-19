"""
Node pure functions to get blocks around a specific time or a block from a block number.
It dosn't use explorers/scanners.

Them return blocks, no block numbers. But you have block.number or block.timestamp available.
"""
from defabipedia import Chain
from karpatkit.node import get_node
from datetime import datetime
import time

max_iterations = 30


def block_for_number(blockchain: Chain, block_number: int):
    """
    Return just the block for a given blockchain and block_number, using the default node for that blockchain.
    """
    node = get_node(blockchain)
    return node.eth.get_block(block_number)


def blocks_around_time(blockchain: Chain, timestamp: float | int, iterations: int = None, precise=True):
    """
    Return two blocks, the closest previous and the closest before blocks around a given timestamp.
    This is an iterative algorith which implements a linear estimator plus a pivot estimator.
    The iteration are limited by defaut to `max_iterations` or the user defined `iterations`.
    """
    node = get_node(blockchain)

    left_block = node.eth.get_block(1)
    right_block = node.eth.get_block("latest")

    def linear_estimate_block(left, right):
        n, block_rate = linear_estimation(left.number, right.number, left.timestamp, right.timestamp, timestamp)
        estimated_block_number = int(round(n))
        return node.eth.get_block(estimated_block_number), block_rate

    def pivot_block(block, block_rate):
        time_error = timestamp - block.timestamp
        estimated_block_number = int(round(block.number + 2*time_error*block_rate))
        return node.eth.get_block(estimated_block_number)

    for it in range(iterations or max_iterations):
        if (it % 2) == 0:
            estimated_block, block_rate = linear_estimate_block(left_block, right_block)
        else:
            estimated_block = pivot_block(estimated_block, block_rate)

        if estimated_block.timestamp < timestamp:
            left_block = estimated_block
        elif estimated_block.timestamp > timestamp:
            right_block = estimated_block
        else:
            return estimated_block, estimated_block

        if (right_block.number - left_block.number) == 1:
            return left_block, right_block

    if precise:
        raise RuntimeError("Result has more than 1 block of distance.")
    else:
        return left_block, right_block


def linear_estimation(n0, n1, t0, t1, t) -> tuple[float, float]:
    r = (n1 - n0) / (t1 - t0)
    n = r * (t - t0) + n0
    return n, r
