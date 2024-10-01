import requests
import json
from web3 import Web3
from karpatkit.node import get_node
from defabipedia.types import Chain
from karpatkit.constants import ABI_TOKEN_SIMPLIFIED, Address
import re

def fetch_abi(contract_address, api_key, chain):
    if chain.upper() == 'POLYGON':
        url = f'https://api.polygonscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}'
    if chain.upper() == 'ETHEREUM':
        url = f'https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}'
    if chain.upper() == 'ARBITRUM':
        url = f'https://api.arbiscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}'
    response = requests.get(url)
    result = response.json()
    if result['status'] == '1':
        return result['result']
    else:
        print(f"Error for {contract_address}: {result['message']}")
        return None
    
def get_implementation_address(web3, contract_address):
     # Use bytes.fromhex instead of Web3.toBytes
    storage_slot = bytes.fromhex("360894A13BA1A3210667C828492DB98DCA3E2076CC3735A920A3CA505D382BBC")
    raw_implementation_address = web3.eth.get_storage_at(contract_address, Web3.to_int(storage_slot))
    if raw_implementation_address != b'\x00' * 32:
        return web3.to_checksum_address(raw_implementation_address[-20:].hex())
    return None


def get_contract_name(web3, contract_address, abi):
    contract = web3.eth.contract(address=contract_address, abi=abi)
    try:
        return contract.functions.name().call()
    except:
        return contract_address

def save_abi_to_file(contract_name, abi_json):
    filename = f'{contract_name}.json'
    with open(filename, 'w') as file:
        json.dump(abi_json, file, indent=4)
    print(f'ABI saved to {filename}')

def main():
    if chain.upper() == 'POLYGON':
        web3 = get_node(Chain.POLYGON) # Connect to a Polygon node
        api_key = 'KPWNSAEG9FJR6B1REG2CIUZII3S7UV6QFP'  # Replace with your PolygonScan API key
    if chain.upper() == 'ETHEREUM':
        web3 = get_node(Chain.ETHEREUM) # Connect to an Ethereum node
        api_key = 'V7CRSQN8M1PGEK27EFAVYHN5TI64HRICYC'
    if chain.upper() == 'ARBITRUM':
        web3 = get_node(Chain.ARBITRUM) # Connect to an Ethereum node
        api_key = 'P7HW6RTZHRAM5GPEIPJWJYSYG8NAYGYW4J'
    contract_addresses = ['0xA5EDBDD9646f8dFF606d7448e414884C7d905dCA', 
'0x9aB958D306Beb81711e5f5CA0731C1E4772dF9cb', 
'0x1B2E88cC7365d90e7E81392432482925BD8437E9', 
'0xb21b06D71c75973babdE35b49fFDAc3F82Ad3775', 
'0x8495AF03fb797E2965bCB42Cb0693e1c15614798', 
'0xD10b40fF1D92e2267D099Da3509253D9Da4D715e', 
'0xe2AA5194E45B043AfdD6E98F467c0B1c13484ae9', 
'0x3fB4d38ea7EC20D91917c09591490Eeda38Cf88A', 
'0x42480C37B249e33aABaf4c22B20235656bd38068', 
'0x88730d254A2f7e6AC8388c3198aFd694bA9f7fae', 
'0xbdE8F31D2DdDA895264e27DD990faB3DC87b372d', 
        ]

    for address in contract_addresses:
        if address != Web3.to_checksum_address(address):
            address = Web3.to_checksum_address(address) # Convert to checksummed address"""
        print(f'Processing contract: {address}')
        
        # First, check if the contract is a proxy
        implementation_address = get_implementation_address(web3, address)
        if implementation_address:
            print('proxy')
        
        # Use the implementation address if it's a proxy; otherwise, use the original address
        target_address = implementation_address if implementation_address else address
        
        abi = fetch_abi(target_address, api_key, chain)
        if abi:
            abi_json = json.loads(abi)
            # Get contract name
            contract_name = get_contract_name(web3, target_address, abi_json)
            # Save the ABI using the contract name
            save_abi_to_file(contract_name, abi_json)
        else:
            print(f'Failed to retrieve ABI for {address}.')

def is_valid_ethereum_address(addr):
    """Check if the provided string is a valid Ethereum address."""
    return re.match(r"^0x[a-fA-F0-9]{40}$", addr) is not None

chain = input('Input Chain: ')
"""api_key = input('Input your API key: ')"""
"""contract_addresses = input('Input contract addresses: ').strip()
if not contract_addresses:
    print("Input cannot be empty.")
elif not contract_addresses.startswith("0x") or len(contract_addresses) != 42:
    print(f'Invalid Ethereum address format: {contract_addresses}')
else:
    # Validate using regex for thorough validation
    if is_valid_ethereum_address(contract_addresses):
        # Convert to checksummed address
        checksummed_address = Web3.to_checksum_address(contract_addresses)
        print(f'Valid Ethereum address: {contract_addresses}')
        print(f'Checksummed Address: {checksummed_address}')
    else:
        print(f'Invalid Ethereum address format: {contract_addresses}')"""
main()

