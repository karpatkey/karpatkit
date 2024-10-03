import json
import re

import requests
from web3 import Web3

from defabipedia.types import Chain
from karpatkit.constants import ABI_TOKEN_SIMPLIFIED, Address
from karpatkit.node import get_node


def fetch_abi(contract_address, api_key, chain):
    if chain.upper() == "POLYGON":
        url = (
            f"https://api.polygonscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
        )
    if chain.upper() == "ETHEREUM":
        url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    if chain.upper() == "ARBITRUM":
        url = f"https://api.arbiscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    if chain.upper() == "OPTIMISM":
        url = f"https://api-optimistic.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    if chain.upper() == "SCROLL":
        url = f"https://api.scroll.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    if chain.upper() == "BASE":
        url = f"https://api.basescan.org/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    response = requests.get(url)
    result = response.json()
    if result["status"] == "1":
        return result["result"]
    else:
        print(f"Error for {contract_address}: {result['message']}")
        return None


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
    except:
        return contract_address


def save_abi_to_file(address, abi_json):
    filename = f"{address}.json"
    with open(filename, "w") as file:
        json.dump(abi_json, file, indent=4)


def main():
    if chain.upper() == "POLYGON":
        web3 = get_node(Chain.POLYGON)  # Connect to a Polygon node
        api_key = "KPWNSAEG9FJR6B1REG2CIUZII3S7UV6QFP"  # Replace with your PolygonScan API key
    if chain.upper() == "ETHEREUM":
        web3 = get_node(Chain.ETHEREUM)  # Connect to an Ethereum node
        api_key = "V7CRSQN8M1PGEK27EFAVYHN5TI64HRICYC"
    if chain.upper() == "ARBITRUM":
        web3 = get_node(Chain.ARBITRUM)  # Connect to an Arbitrum node
        api_key = "P7HW6RTZHRAM5GPEIPJWJYSYG8NAYGYW4J"
    if chain.upper() == "OPTIMISM":
        web3 = get_node(Chain.OPTIMISM)  # Connect to a Optimism node
        api_key = "7KHS47QYPX8IDIZR5E2F4S9NWWG3NDXJ67"
    if chain.upper() == "BASE":
        web3 = get_node(Chain.BASE)  # Connect to a Base node
        api_key = "ARQ6TZ2DIPGNN6H2PRKH1YHV6U486JJIY9"
    """if chain.upper() == 'SCROLL':
        web3 = get_node(Chain.SCROLL) # Connect to a Scroll node
        api_key = 'TPFPXF2MEANHGI8EF8P6PI96YXQM4DAN3H'"""

    """contract_addresses = ['0xA5EDBDD9646f8dFF606d7448e414884C7d905dCA', 
'0x9aB958D306Beb81711e5f5CA0731C1E4772dF9cb',  
        ]"""

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
"""api_key = input('Input your API key: ')"""
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
