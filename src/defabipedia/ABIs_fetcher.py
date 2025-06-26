import json
import re

import requests
from web3 import Web3

from defabipedia.types import Blockchain, Chain
from karpatkit.node import get_node

BASE_URL = "https://api.etherscan.io/v2/api"


def _get_chain_id(chain: str | Blockchain) -> int:
    """
    Resolve a chain name (e.g. "polygon") or a Blockchain instance to its chain_id.
    """
    if isinstance(chain, Blockchain):
        return chain.chain_id

    if isinstance(chain, str):
        attr = chain.upper()
        if hasattr(Chain, attr):
            return getattr(Chain, attr).chain_id

    raise ValueError(f"Unsupported chain: {chain}")

def fetch_abi(contract_address: str, api_key: str, chain: str | Blockchain) -> str:
    """
    Fetch the verified ABI of *contract_address* on the specified chain
    using the Etherscan V2 API.
    """
    chain_id = _get_chain_id(chain)

    url = (
        f"{BASE_URL}"
        f"?chainid={chain_id}"
        f"&module=contract"
        f"&action=getabi"
        f"&address={contract_address}"
        f"&apikey={api_key}"
    )

    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    if data.get("status") != "1":
        raise RuntimeError(
            f"Etherscan error for {contract_address} on chain {chain_id}: "
            f"{data.get('message')} – {data.get('result')}"
        )

    return data["result"]



def get_implementation_address(web3, contract_address):
    # Use bytes.fromhex instead of Web3.toBytes
    storage_slot = bytes.fromhex("360894A13BA1A3210667C828492DB98DCA3E2076CC3735A920A3CA505D382BBC")
    raw_implementation_address = web3.eth.get_storage_at(contract_address, Web3.to_int(storage_slot))
    if raw_implementation_address != b"\x00" * 32:
        return web3.to_checksum_address(raw_implementation_address[-20:].hex())
    return None


def get_contract_name(web3, contract_address, abi):
    contract = web3.eth.contract(address=contract_address, abi=abi)
    try:
        return contract.functions.name().call()
    except:  # noqa
        return contract_address


def save_abi_to_file(address, abi_json):
    filename = f"{address}.json"
    with open(filename, "w") as file:
        json.dump(abi_json, file, indent=4)


def main():
    if chain.upper() == "POLYGON":
        web3 = get_node(Chain.POLYGON)  # Connect to a Polygon node
    if chain.upper() == "ETHEREUM":
        web3 = get_node(Chain.ETHEREUM)  # Connect to an Ethereum node
    if chain.upper() == "ARBITRUM":
        web3 = get_node(Chain.ARBITRUM)  # Connect to an Arbitrum node
    if chain.upper() == "OPTIMISM":
        web3 = get_node(Chain.OPTIMISM)  # Connect to a Optimism node
    if chain.upper() == "BASE":
        web3 = get_node(Chain.BASE)  # Connect to a Base node
    """if chain.upper() == 'SCROLL':
        web3 = get_node(Chain.SCROLL) # Connect to a Scroll node
        api_key = 'TPFPXF2MEANHGI8EF8P6PI96YXQM4DAN3H'"""

    """contract_addresses = ['0xA5EDBDD9646f8dFF606d7448e414884C7d905dCA',
                            '0x9aB958D306Beb81711e5f5CA0731C1E4772dF9cb']"""

    for address in checksummed_addresses:
        print(f"Processing contract: {address}")

        # First, check if the contract is a proxy
        implementation_address = get_implementation_address(web3, address)
        if implementation_address:
            print("proxy")
            if implementation_address != Web3.to_checksum_address(implementation_address):
                implementation_address = Web3.to_checksum_address(address)  # Convert to checksummed address"""
        # Use the implementation address if it's a proxy; otherwise, use the original address
        target_address = implementation_address if implementation_address else address

        abi = fetch_abi(target_address, api_key, chain)
        if abi:
            abi_json = json.loads(abi)
            # Save the ABI using the address
            save_abi_to_file(address, abi_json)
            if target_address != address:
                print(f"ABI of {target_address} saved as {address}.")
            else:
                print(f"ABI of {address} saved.")
        else:
            print(f"Failed to retrieve ABI for {address}.")


def is_valid_ethereum_address(addr):
    """Check if the provided string is a valid Ethereum address."""
    return re.match(r"^0x[a-fA-F0-9]{40}$", addr) is not None


chain = input("Input Chain: ")
api_key = input('Input your API key: ')
addresses_input = input("Input contract addresses: ")
checksummed_addresses = []
contract_addresses = [address.strip() for address in addresses_input.split(",")]
print(contract_addresses)
if not contract_addresses:
    print("Input cannot be empty.")
for address in contract_addresses:
    if not address.startswith("0x") or len(address) != 42:
        print(f"Invalid Ethereum address format: {address}")
    if is_valid_ethereum_address(address):  # Validate using regex for thorough validation
        # Convert to checksummed address
        address = Web3.to_checksum_address(address)
        checksummed_addresses.append(address)
    else:
        print(f"Invalid Ethereum address format: {address}")
print(checksummed_addresses)
main()
