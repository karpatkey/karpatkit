"""
Node pure functions to get blocks around a specific time or a block from a block number.
It dosn't use explorers/scanners.

Them return blocks, no block numbers. But you have block.number or block.timestamp available.
"""
import time
from datetime import datetime

from defabipedia import Chain
from karpatkit.node import get_node

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
        estimated_block_number = int(round(block.number + 2 * time_error * block_rate))
        return node.eth.get_block(estimated_block_number)

    print()

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

        # print(f"{it=:3d}|number={estimated_block.number:10_d}|timestamp={estimated_block.timestamp:14f}|period={1/block_rate:4.1f}|")
        print(
            f"{it=:3d}|left={left_block.number:10_d}|right={right_block.number:10_d}|timestamp={estimated_block.timestamp:14f}|period={1/block_rate:4.1f}|"
        )
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


def newton_mauro(f, iterations, n_min, n_max):
    """
    Improved Newton-Raphson method for monotonic and discret functions. Search n for f(n)=0
    """
    n_left = n_prev = n_min
    n_right = n = n_max

    fn_prev = f(n_prev)
    for it in range(iterations):
        fn = f(n)
        if it == 0 and fn * fn_prev > 0:
            raise IndexError("No solution: f(n) for n in [n_min, n_max] isn't expected to have a cross with zero.")

        if n == n_prev or abs(n - n_prev) == 1 and (fn * fn_prev) <= 0:
            break

        if fn > 0:
            n_right = n
        elif fn < 0:
            n_left = n
        else:
            break

        dfn = (fn - fn_prev) / (n - n_prev)

        if dfn == 0:
            break

        print(f"\n{it=:3d}|{n=:10_d}|{fn=:14.1f}|{dfn=:4.1f}|", end="")
        n_prev = n
        n = int(round(n - fn / dfn))
        if n <= n_left:
            n = n_left + 1
        if n >= n_right:
            n = n_right - 1
        fn_prev = fn

    return n


def blocks_around_time(blockchain: Chain, timestamp: float | int, iterations: int = None, precise=True):
    from functools import cache

    node = get_node(blockchain)
    get_block = cache(node.eth.get_block)
    f = lambda n: get_block(n).timestamp - timestamp
    n = newton_mauro(f, iterations or max_iterations, n_min=1, n_max=get_block("latest").number - 1)
    b = get_block(n)
    return (b, get_block(n + 1)) if f(n) < timestamp else (get_block(n - 1), b)


def newton_raphson(f, iterations, n_min, n_max, moving_avg=4):
    """
    Search n for f(n)=0
    """
    n_prev = n_min
    n = n_max
    dfns = []

    fn_prev = f(n_prev)
    print()
    print(f"it= -2|n={n_prev:5_d}|")
    print(f"it= -1|{n=:10_d}|")
    for it in range(iterations):
        fn = f(n)

        if n == n_prev or abs(n - n_prev) == 1 and (fn * fn_prev) <= 0:
            break

        dfns = [(fn - fn_prev) / (n - n_prev), *dfns[: moving_avg - 1]]
        dfn = sum(dfns) / len(dfns)

        print(f"{it=:3d}|{n=:10_d}|{fn=:14.1f}|{dfn=:4.1f}|")

        n_prev = n
        n = int(round(n - fn / dfn))
        if n < n_min:
            n = n_min
        if n > n_max:
            n = n_max
        fn_prev = fn

    return n
