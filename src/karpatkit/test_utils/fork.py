import atexit
import codecs
import gzip
import json
import logging
import os
import shlex
import shutil
import socket
import subprocess
import time
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import pytest
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import AsyncWeb3, HTTPProvider, Web3
from web3._utils.encoding import Web3JsonEncoder
from web3.exceptions import ContractLogicError
from web3.middleware import Web3Middleware
from web3.providers import AsyncHTTPProvider
from web3.providers.base import BaseProvider

from defabipedia import Blockchain, Chain
from defabipedia.tokens import erc20_contract

from .simple_safe import SimpleSafe

logger = logging.getLogger(__name__)


@dataclass
class ForkConfig:
    upstream_url: str
    default_block: int
    local_port: int
    blockchain: Blockchain


REMOTE_ETH_NODE_URL = codecs.decode(
    b"x\x9c\xcb())(\xb6\xd2\xd7O-\xc9\xd0\xcdM\xcc\xcc\xcbK-\xd1K\xd7K\xccI\xceH\xcd\xad\xd4K\xce\xcf\xd5/3\xd2\x0f"
    b"u)74-6NNu\xb3\xcc\x0f\nH\n\xcb\xccq4\xd4u\xcd3(53+\xf32\n(\x06\x00Q\x92\x17X",
    "zlib",
).decode()
REMOTE_GC_NODE_URL = "https://rpc.gnosischain.com"
REMOTE_BASE_NODE_URL = "https://1rpc.io/base"
REMOTE_OPT_NODE_URL = "https://1rpc.io/op"
REMOTE_ARB_NODE_URL = "https://arb1.arbitrum.io/rpc"

RUN_LOCAL_NODE = os.environ.get("KKIT_RUN_LOCAL_NODE", False)

eth_fork_cfg = ForkConfig(
    upstream_url=os.environ.get("KKIT_ETH_FORK_URL", REMOTE_ETH_NODE_URL),
    local_port=8546,
    default_block=17565000,
    blockchain=Chain.ETHEREUM,
)

gc_fork_cfg = ForkConfig(
    upstream_url=os.environ.get("KKIT_GC_FORK_URL", REMOTE_GC_NODE_URL),
    local_port=8547,
    default_block=30397769,
    blockchain=Chain.GNOSIS,
)

base_fork_cfg = ForkConfig(
    upstream_url=os.environ.get("KKIT_BASE_FORK_URL", REMOTE_BASE_NODE_URL),
    local_port=8548,
    default_block=21744030,
    blockchain=Chain.BASE,
)

opt_fork_cfg = ForkConfig(
    upstream_url=os.environ.get("KKIT_OPT_FORK_URL", REMOTE_OPT_NODE_URL),
    local_port=8549,
    default_block=127339335,
    blockchain=Chain.OPTIMISM,
)

arb_fork_cfg = ForkConfig(
    upstream_url=os.environ.get("KKIT_ARB_FORK_URL", REMOTE_ARB_NODE_URL),
    local_port=8550,
    default_block=269169232,
    blockchain=Chain.ARBITRUM,
)

fork_configs = {
    Chain.ETHEREUM: eth_fork_cfg,
    Chain.GNOSIS: gc_fork_cfg,
    Chain.BASE: base_fork_cfg,
    Chain.OPTIMISM: opt_fork_cfg,
    Chain.ARBITRUM: arb_fork_cfg,
}


def get_local_web3_url_for_chain(blockchain: Blockchain):
    cfg = fork_configs[blockchain]
    return f"http://127.0.0.1:{cfg.local_port}"


@lru_cache(maxsize=24)
def get_local_web3_for_chain(blockchain: Blockchain):
    return Web3(HTTPProvider(get_local_web3_url_for_chain(blockchain), request_kwargs={"timeout": 30}))


@lru_cache(maxsize=24)
def get_local_async_web3_for_chain(blockchain: Blockchain):
    return AsyncWeb3(AsyncHTTPProvider(get_local_web3_url_for_chain(blockchain), request_kwargs={"timeout": 30}))


def gen_test_accounts() -> list[LocalAccount]:
    # test accounts are generated using the mnemonic:
    #   "test test test test test test test test test test test junk" and derivation path "m/44'/60'/0'/0"
    keys = [
        "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80",
        "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d",
        "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a",
        "0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6",
        "0x47e179ec197488593b187f80a00eb0da91f1b9d0b13f8733639f19c30a34926a",
        "0x8b3a350cf5c34c9194ca85829a2df0ec3153be0318b5e2d3348e872092edffba",
        "0x92db14e403b83dfe3df233f83dfa3a0d7096f21ca9b0d6d6b8d88b2b4ec1564e",
        "0x4bbbf85ce3377467afe5d46f804f221813b2bb87f24d81f60f1fcdbf7cbf4356",
        "0xdbda1821b80551c9d65939329250298aa3472ba22feea921c0cf5d620ea67b97",
        "0x2a871d0798f97d79848a013d4936a73bf4cc922c825d33c1cf7073dff6d409c6",
    ]
    return [Account.from_key(key) for key in keys]


TEST_ACCOUNTS = gen_test_accounts()
SCRAPE_ACCOUNT = Account.from_key("0xf214f2b2cd398c806f84e317254e0f0b801d0643303237d97a22a48e01628897")


def wait_for_port(port, host="localhost", timeout=5.0):
    """Wait until a port starts accepting TCP connections."""
    start_time = time.time()
    while True:
        try:
            s = socket.create_connection((host, port), timeout=timeout)
            s.close()
            return
        except OSError as exc:
            time.sleep(0.05)
            if time.time() - start_time >= timeout:
                raise OSError("Timeout waiting for port") from exc


class SimpleDaemonRunner:
    def __init__(self, cmd, popen_kwargs=None):
        self.console = None
        self.proc = None
        self.cmd = cmd
        self.popen_kwargs = popen_kwargs or {}

    def start(self):
        if self.is_running():
            raise ValueError("Process is already running")
        logger.info("Starting daemon: %s %s", self.cmd, self.popen_kwargs)
        self.proc = subprocess.Popen(shlex.split(self.cmd), **self.popen_kwargs)
        atexit.register(self.stop)

    def stop(self):
        if not self.proc:
            return

        self.proc.terminate()
        stdout, stderr = self.proc.communicate(timeout=20)
        retcode = self.proc.returncode

        self.proc = None
        return retcode

    def is_running(self):
        return self.proc is not None


def fork_unlock_account(w3, address):
    """Unlock the given address on the forked node."""
    return w3.provider.make_request("anvil_impersonateAccount", [address])


def fork_set_balance(w3, address, amount):
    return w3.provider.make_request("anvil_setBalance", [address, amount])


def fork_reset_state(w3: Web3, url: str, block: int | str = "latest"):
    """Reset the state of the forked node to the state of the blockchain node at the given block.

    Args:
        w3: Web3 instance of the local node
        url: URL of the node from which to fork
        block: Block number at which to fork the blockchain, or "latest" to use the latest block
    """

    if isinstance(block, str) and block == "latest":
        raise ValueError("Can't use 'latest' as fork block")
    return w3.provider.make_request("anvil_reset", [{"forking": {"jsonRpcUrl": url, "blockNumber": block}}])


def run_hardhat(url, block, port):
    """Run hardhat node in the background."""
    try:
        npm = shutil.which("npm")
        subprocess.check_call([npm, "--version"])
        if "hardhat" not in json.loads(subprocess.check_output([npm, "list", "--json"])).get("dependencies", {}):
            raise subprocess.CalledProcessError
    except subprocess.CalledProcessError:
        raise RuntimeError("Hardhat is not installed properly. Check the README for instructions.") from None

    log_filename = "/tmp/rr_hardhat_log.txt"
    logger.info(f"Writing Hardhat log to {log_filename}")
    hardhat_log = open(log_filename, "w")  # noqa: SIM115
    npx = shutil.which("npx")
    node = SimpleDaemonRunner(
        cmd=f"{npx} hardhat node --show-stack-traces --fork '{url}' --fork-block-number {block} --port {port}",
        popen_kwargs={"stdout": hardhat_log, "stderr": hardhat_log},
    )
    node.start()
    return node


def run_anvil(url, block, port):
    """Run anvil node in the background with version check"""
    log_filename = f"/tmp/rr_fork_node_{port}_log.txt"
    logger.info(f"Writing Anvil log to {log_filename}")
    log = open(log_filename, "w")  # noqa: SIM115

    # version can also be "0.3.0=stable so this doesn't work"
    # version = subprocess.run(["anvil", "--version"], capture_output=True, text=True).stdout

    # year, month, _ = version.split()[3].split("-")

    # if not (int(year) >= 2024 and int(month) >= 9):
    #     raise RuntimeError(f"Anvil version is too old: {version}. Minimum required is 2024-09.")

    node = SimpleDaemonRunner(
        cmd=f"anvil --accounts 15 -f '{url}' --fork-block-number {block} --port {port} "
        f"--hardfork latest --timeout 30000",
        popen_kwargs={"stdout": log, "stderr": log},
    )

    node.start()
    return node


class LocalNode:
    def __init__(self, fork_cfg: ForkConfig):
        self.fork_cfg = fork_cfg
        self.port = fork_cfg.local_port
        self.url = f"http://127.0.0.1:{fork_cfg.local_port}"
        self.default_block = fork_cfg.default_block
        self.w3 = Web3(HTTPProvider(self.url, request_kwargs={"timeout": 30}))
        self.w3_async = AsyncWeb3(AsyncHTTPProvider(self.url, request_kwargs={"timeout": 30}))

    def reset_state(self):
        fork_reset_state(self.w3, self.fork_cfg.upstream_url, self.default_block)

    def unlock_account(self, address: str):
        fork_unlock_account(self.w3, address)

    def set_block(self, block):
        """Set the local node to a specific block"""
        fork_reset_state(self.w3, url=self.fork_cfg.upstream_url, block=block)


def _local_node(request, node: LocalNode):
    """Run a local node_daemon for testing"""
    if RUN_LOCAL_NODE:
        node_daemon = run_anvil(node.fork_cfg.upstream_url, node.default_block, node.fork_cfg.local_port)

        def stop():
            node_daemon.stop()

        request.addfinalizer(stop)

    wait_for_port(node.port, timeout=20)

    class LatencyMeasurerMiddleware(Web3Middleware):
        def __init__(self, w3):
            self.w3 = w3


    node.w3.middleware_onion.add(LatencyMeasurerMiddleware, "latency_middleware")
    node.reset_state()
    return node


def steal_token(w3, token, holder, to, amount):
    """Steal tokens from a holder sending them to another address (sends 1 ETH to the holder first)"""
    fork_unlock_account(w3, holder)
    top_up_address(w3=w3, address=holder, amount=1)
    ctract = erc20_contract(w3, token)
    tx = ctract.functions.transfer(to, amount).transact({"from": holder})
    return tx


def create_simple_safe(w3: Web3, owner: LocalAccount) -> SimpleSafe:
    """Create a Safe with one owner and 1 ETH in balance"""

    safe = SimpleSafe.build(owner, w3)
    top_up_address(w3=w3, address=safe.address, amount=1)
    fork_unlock_account(w3, safe.address)
    return safe


def top_up_address(w3: Web3, address: str, amount: int) -> None:
    """Top up an address with ETH"""
    if amount > (w3.eth.get_balance(SCRAPE_ACCOUNT.address) * 1e18) * 0.99:
        raise ValueError("Not enough ETH in the faucet account")
    try:
        w3.eth.send_transaction({"to": address, "value": Web3.to_wei(amount, "ether"), "from": SCRAPE_ACCOUNT.address})
    except ContractLogicError as exc:
        raise Exception("Address is a smart contract address with no payable function.") from exc


def steal_safe(w3: Web3, safe_address: str, new_owner_local_account: LocalAccount) -> SimpleSafe:
    """
    Return a SimpleSafe instance from an existing safe with a new owner.

    The new owner will be added to the owners list, and the threshold will be set to 1,
    so it will be able to sign and execute transactions.
    """

    safe = SimpleSafe(safe_address, w3=w3, signer_key=new_owner_local_account.key)

    fork_unlock_account(w3, safe_address)
    fork_set_balance(w3, safe.address, 10000000000000000000)  # give some gas: 10 ETH

    # set threshold to 1 and add owner
    safe.contract.functions.addOwnerWithThreshold(new_owner_local_account.address, 1).transact({"from": safe.address})
    return safe


@pytest.fixture(scope="session")
def local_node_eth(request) -> LocalNode:
    node = LocalNode(eth_fork_cfg)
    _local_node(request, node)
    return node


@pytest.fixture(scope="session")
def local_node_gc(request) -> LocalNode:
    node = LocalNode(gc_fork_cfg)
    _local_node(request, node)
    return node


@pytest.fixture(scope="session")
def local_node_base(request) -> LocalNode:
    node = LocalNode(base_fork_cfg)
    _local_node(request, node)
    return node


@pytest.fixture(scope="session")
def local_node_opt(request) -> LocalNode:
    node = LocalNode(opt_fork_cfg)
    _local_node(request, node)
    return node


@pytest.fixture(scope="session")
def local_node_arb(request) -> LocalNode:
    node = LocalNode(arb_fork_cfg)
    _local_node(request, node)
    return node


@pytest.fixture(scope="session")
def accounts() -> list[LocalAccount]:
    return TEST_ACCOUNTS


class RecordMiddleware(Web3Middleware):
    interactions = []

    def __init__(self, w3):
        self.w3 = w3

    @classmethod
    def clear_interactions(cls):
        cls.interactions = []



class ReplayAndAssertMiddleware(Web3Middleware):
    interactions = None

    @classmethod
    def set_interactions(cls, interactions: list):
        cls.interactions = list(reversed(interactions))

    def __init__(self, w3):
        self.w3 = w3



class DoNothingWeb3Provider(BaseProvider):
    def __init__(self, chain_id):
        self.chain_id = chain_id

    def make_request(self, method, params):
        if method == "eth_chainId":
            return {"jsonrpc": "2.0", "id": 1, "result": hex(self.chain_id)}


class DoNothingLocalNode:
    def __init__(self, chain_id):
        self.w3 = Web3(DoNothingWeb3Provider(chain_id))

    def reset_state(self):
        pass

    def unlock_account(self, address: str):
        pass

    def set_block(self, block):
        pass


def _local_node_replay(local_node, request):
    chain = local_node.fork_cfg.blockchain
    if "record" not in local_node.w3.middleware_onion:
        local_node.w3.middleware_onion.inject(RecordMiddleware, "record", layer=0)

    test_file_path = Path(request.node.path)
    directory = test_file_path.parent.resolve()
    test_name = request.node.name
    filename = f"{test_file_path.name}-{test_name}-{chain.name}.json.gz"
    web3_test_data_file = directory / "test_data" / filename

    mode = "replay_and_assert" if os.path.exists(web3_test_data_file) else "record"

    if not web3_test_data_file.parent.exists():
        os.makedirs(web3_test_data_file.parent)

    RecordMiddleware.clear_interactions()

    if mode == "replay_and_assert":
        with gzip.open(web3_test_data_file, mode="rt") as f:
            ReplayAndAssertMiddleware.set_interactions(json.load(f))
        fake_local_node = DoNothingLocalNode(chain.chain_id)
        fake_local_node.w3.middleware_onion.inject(ReplayAndAssertMiddleware, "replay_and_assert", layer=0)
        yield fake_local_node
    else:
        yield local_node

    local_node.w3.middleware_onion.remove("record")

    if mode == "record":
        # TODO: don't write the file if the test failed
        # https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
        data = json.dumps(RecordMiddleware.interactions, indent=2, cls=Web3JsonEncoder)
        with gzip.open(web3_test_data_file, mode="wt") as f:
            f.write(data)


@pytest.fixture()
def local_node_eth_replay(local_node_eth, request) -> LocalNode:
    yield from _local_node_replay(local_node_eth, request)


@pytest.fixture()
def local_node_gc_replay(local_node_gc, request) -> LocalNode:
    yield from _local_node_replay(local_node_gc, request)


@pytest.fixture()
def local_node_base_replay(local_node_base, request) -> LocalNode:
    yield from _local_node_replay(local_node_base, request)


@pytest.fixture()
def local_node_opt_replay(local_node_opt, request) -> LocalNode:
    yield from _local_node_replay(local_node_opt, request)


@pytest.fixture()
def local_node_arb_replay(local_node_arb, request) -> LocalNode:
    yield from _local_node_replay(local_node_arb, request)
