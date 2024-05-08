"""
Node pure functions to search blocks around a specific time. It doesn't use explorers/scanners.

This functions return a Block object, defined here, with `block.number` and `block.timestamp`. `timestamp`s are defined
in seconds from the Unix/POSIX epoch.

The main user function is `all_chains_block_before_time`. It search all chains block in parallel. But, if you want
to search a block just for one blockchain, you can use `block_before_time`.
"""
import asyncio
import logging
from dataclasses import dataclass
from functools import cache

from defabipedia import Blockchain, Chain
from karpatkit.node import get_node

logger = logging.getLogger(__name__)

max_iterations = 30  # times
latest_block_number_margin = 30  # backward blocks from the latest block


@dataclass(frozen=True)
class Block:
    number: int
    timestamp: float

    @classmethod
    def from_web3(cls, web3_block):
        return cls(number=web3_block.number, timestamp=web3_block.timestamp)


def all_chains_block_before_time(timestamp: float = None) -> dict[Blockchain, Block]:
    """
    Return a dict with {blockchain: block} where block is the closest block before timestamp, for all blockchains.
    This function skips results with errors, but log them.
    If `timestamp` isn't defined, the latest block is returned.
    """
    if timestamp is None:
        async_all_chains_coro = async_all_chains_get_latest_block()
    else:
        async_all_chains_coro = async_all_chains_block_before_time(timestamp=timestamp)
    d = dict()
    for chain, block in asyncio.run(async_all_chains_coro).items():
        if isinstance(block, Exception):
            error = block
            logger.error(f"For {chain}: {error!r}")
        else:
            d[chain] = block
    return d


async def async_all_chains_block_before_time(timestamp: float) -> dict[Blockchain, Block | Exception]:
    return await async_all_chains(block_before_time, timestamp=timestamp)


async def async_all_chains_get_latest_block() -> dict[Blockchain, Block | Exception]:
    return await async_all_chains(get_latest_block)


async def async_all_chains(func, **kwargs) -> dict[Blockchain, Block | Exception]:
    chains = Chain.all()
    results = await asyncio.gather(
        *(asyncio.to_thread(func, blockchain=blockchain, **kwargs) for blockchain in chains),
        return_exceptions=True,
    )
    return dict(zip(chains, results))


def block_before_time(blockchain: Blockchain, timestamp: float) -> Block:
    """
    Return the closest previous for a given timestamp.
    This uses an iterative algorithm, limited by the global `max_iterations`.
    """
    return blocks_around_time(blockchain, timestamp)[0]


def blocks_around_time(blockchain: Blockchain, timestamp: float) -> tuple[Block, Block]:
    """
    Return two blocks, the closest previous and subsequent blocks around a given timestamp.
    This uses an iterative algorithm, limited by the global `max_iterations`.
    """

    def f(n):
        return get_block(blockchain, n).timestamp - timestamp

    block_before, block_after = discret_newton_raphson(
        f, max_iterations, n_min=1, n_max=get_latest_block_number(blockchain)
    )
    return get_block(blockchain, block_before), get_block(blockchain, block_after)


@cache
def get_block(blockchain: Blockchain, block_number: int) -> Block:
    """
    Return just the block for a given blockchain and block_number, using the default node for that blockchain.
    """
    assert isinstance(block_number, int)
    node = get_node(blockchain)
    return Block.from_web3(node.eth.get_block(block_number))


def get_latest_block_number(blockchain: Blockchain) -> int:
    node = get_node(blockchain)
    return node.eth.get_block("latest").number - latest_block_number_margin


def get_latest_block(blockchain: Blockchain) -> Block:
    return get_block(blockchain, get_latest_block_number(blockchain))


def discret_newton_raphson(f, max_iterations, n_min, n_max):
    """
    Improved Newton-Raphson method for monotonic and discret functions. Search n for f(n)=0.
    The null derivative is managed better than in newton_raphson.
    """
    n_left = n_prev = n_min
    n_right = n = n_max

    fn_prev = f(n_prev)
    for it in range(max_iterations):
        fn = f(n)
        if it == 0 and fn * fn_prev > 0:
            raise IndexError("No solution: f(n) for n in [n_min, n_max] isn't expected to have a cross with zero.")

        if fn >= 0:
            n_right = n
        if fn <= 0:
            n_left = n
        if fn == 0:
            break

        if n == n_prev or abs(n - n_prev) == 1 and (fn * fn_prev) <= 0:
            break

        dfn = (fn - fn_prev) / (n - n_prev)

        # print(f"\n{it=:3d}|{n=:10_d}|{fn=:14.1f}|{dfn=:4.1f}|", end="")

        n_prev = n
        if dfn == 0:
            n = int(round((n_left + n_right) / 2))
        else:
            n = int(round(n - fn / dfn))
            if n <= n_left:
                n = n_left + 1
            if n >= n_right:
                n = n_right - 1
        fn_prev = fn

    return n_left, n_right
