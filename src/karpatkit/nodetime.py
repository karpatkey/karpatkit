"""
Node pure functions to get blocks around a specific time or a block from a block number.
It dosn't use explorers/scanners.

Them return blocks, no block numbers. But you have block.number or block.timestamp available.
"""
from defabipedia import Chain
from karpatkit.node import get_node

max_iterations = 30


def block_for_number(blockchain: Chain, block_number: int):
    """
    Return just the block for a given blockchain and block_number, using the default node for that blockchain.
    """
    node = get_node(blockchain)
    return node.eth.get_block(block_number)


def newton_mauro(f, iterations, n_min, n_max):
    """
    Improved Newton-Raphson method for monotonic and discret functions. Search n for f(n)=0.
    """
    n_left = n_prev = n_min
    n_right = n = n_max

    fn_prev = f(n_prev)
    for it in range(iterations):
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

        print(f"\n{it=:3d}|{n=:10_d}|{fn=:14.1f}|{dfn=:4.1f}|", end="")

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


def newton_raphson(f, iterations, n_min, n_max):
    """
    Search n for f(n)=0
    """
    n_prev = n_min
    n = n_max

    fn_prev = f(n_prev)
    for it in range(iterations):
        fn = f(n)
        if it == 0 and fn * fn_prev > 0:
            raise IndexError("No solution: f(n) for n in [n_min, n_max] isn't expected to have a cross with zero.")

        if n == n_prev or abs(n - n_prev) == 1 and (fn * fn_prev) <= 0:
            break

        dfn = (fn - fn_prev) / (n - n_prev)

        if dfn == 0:
            break

        print(f"\n{it=:3d}|{n=:10_d}|{fn=:14.1f}|{dfn=:4.1f}|", end="")
        n_prev = n
        n = int(round(n - fn / dfn))
        if n < n_min:
            n = n_min
        if n > n_max:
            n = n_max
        fn_prev = fn

    return tuple(sorted([n_prev, n]))


def blocks_around_time(
    blockchain: Chain, timestamp: float, iterations: int = None, search_algorithm=newton_mauro, n_max=None
):
    """
    Return two blocks, the closest previous and the closest before blocks around a given timestamp.
    This is an iterative algorith which implements the linear estimator plus a pivot estimator.
    The iteration are limited by defaut to `max_iterations` or the user defined `iterations`.
    """
    from functools import cache

    node = get_node(blockchain)
    get_block = cache(node.eth.get_block)

    def f(n):
        return get_block(n).timestamp - timestamp

    nl, nr = search_algorithm(f, iterations or max_iterations, n_min=1, n_max=n_max or get_block("latest").number - 1)
    return get_block(nl), get_block(nr)
