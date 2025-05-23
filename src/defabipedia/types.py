import inspect
import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from web3 import Web3

__all__ = ["Blockchain", "Chain", "parent", "ContractSpec", "ContractAbi", "ContractAddress", "StrEnum"]


class StrEnum(str, Enum):
    def __new__(cls, value):
        # values must already be of type `str`
        if not isinstance(value, str):
            raise TypeError(f"{value!r} is not a string")
        value = str(value)
        member = str.__new__(cls, value)
        member._value_ = value
        return member


class Blockchain(str):
    chain_id: int

    def __new__(cls, name: str, chain_id: int):
        instance = super().__new__(cls, name)
        instance.chain_id = chain_id
        return instance

    @property
    def name(self):
        return str(self)


class Chain:
    ETHEREUM = Blockchain("ethereum", 0x1)
    POLYGON = Blockchain("polygon", 0x89)
    AVALANCHE = Blockchain("avalanche", 0xA86A)
    BINANCE = Blockchain("binance", 0x38)
    FANTOM = Blockchain("fantom", 0xFA)
    GNOSIS = Blockchain("gnosis", 0x64)
    ARBITRUM = Blockchain("arbitrum", 0xA4B1)
    OPTIMISM = Blockchain("optimism", 0xA)
    ROPSTEN = Blockchain("ropsten", 0x3)
    GOERLI = Blockchain("goerli", 0x5)
    KOVAN = Blockchain("kovan", 0x45)
    BASE = Blockchain("base", 0x2105)
    METIS = Blockchain("metis", 0x440)
    COSMOS = Blockchain("cosmos", 0xF0C74)

    # Look up indexes
    _by_id = {}
    _by_name = {}
    for attr_value in locals().copy().values():
        if isinstance(attr_value, Blockchain):
            _by_id[attr_value.chain_id] = attr_value
            _by_name[attr_value.name] = attr_value

    @classmethod
    def all(cls):
        return list(cls._by_name.values())

    @classmethod
    def get_blockchain_by_chain_id(cls, chain_id) -> Blockchain:
        try:
            return cls._by_id.get(chain_id, None)
        except KeyError:
            raise ValueError(f"No Blockchain with chain_id {chain_id} found in Chain.") from None

    @classmethod
    def get_blockchain_by_name(cls, name) -> Blockchain | None:
        return cls._by_name.get(name.lower(), None)

    @classmethod
    def get_blockchain_from_web3(cls, w3: Web3) -> Blockchain:
        return cls.get_blockchain_by_chain_id(w3.eth.chain_id)


class ContractAbi:
    abi_path: Path

    def __init__(self, name: str, abi: str | None = None, abi_path: Path | None = None):
        self.name = name
        self._abi = abi  # if no abi is provided the abi_path will be used lazily
        self.abi_path = abi_path or Path("")
        if abi is None and abi_path is None:
            raise ValueError("Missing argument: abi or abi_path must me provided")

    def __str__(self):
        return self.name

    @property
    def abi(self):
        if self._abi is None:
            with open(self.abi_path) as f:
                self._abi = json.load(f)
        return self._abi


class ContractSpec(ContractAbi):
    """
    It refers to a contract's deployment, adding a specific address.
    """

    def __init__(self, address: str, name: str, abi: str | None = None, abi_path: Path | None = None):
        super().__init__(name, abi, abi_path)
        self.address = Web3.to_checksum_address(address)

    def contract(self, w3: Web3):
        return w3.eth.contract(address=self.address, abi=self.abi)


class SwapPools(ContractSpec):
    def __init__(
        self,
        address: str,
        name: str,
        abi: str | None = None,
        abi_path: Path | None = None,
        tokens: list[str] | None = None,
        protocol: str | None = None,
        uni_fee: int = 100,
    ):
        super().__init__(address, name, abi, abi_path)
        self.tokens = tokens or []
        self.protocol = protocol
        self.uni_fee = uni_fee


@dataclass
class ContractAddress:
    name: str
    address: str

    def __str__(self):
        return self.name


def current_dir() -> Path:
    """Return the directory path of the caller. Slow!"""
    caller_frame = inspect.stack()[1]
    return Path(caller_frame.filename).parent


def parent(path) -> Path:
    """Return the directory of a path as a Path object"""
    return Path(path).parent
