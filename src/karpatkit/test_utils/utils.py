from web3 import Web3


def to_hex_32_bytes(value: str | int) -> str:
    """Convert a value to a 32 bytes hex string"""
    if isinstance(value, str):
        if value.startswith("0x") and len(value) <= 66:
            return "0x" + value[2:].rjust(64, "0")
        else:
            raise ValueError("Invalid value. Value must be a hex string with or without 0x prefix and length <= 66")
    elif isinstance(value, int):
        return Web3.to_hex(Web3.to_bytes(value).rjust(32, b"\0"))
    else:
        raise ValueError("Invalid value. Value must be an int or a hex string with 0x prefix and length <= 66")
