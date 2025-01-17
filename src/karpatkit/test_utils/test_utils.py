from .fork import create_simple_safe
from .utils import to_hex_32_bytes


def test_to_hex_32_bytes():
    assert to_hex_32_bytes(15789) == "0x0000000000000000000000000000000000000000000000000000000000003dad"
    assert (
        to_hex_32_bytes("0x51D34416593a8acF4127dc4a40625A8eFAB9940c")
        == "0x00000000000000000000000051D34416593a8acF4127dc4a40625A8eFAB9940c"
    )


def test_create_safe_gnosis(local_node_gc_replay, accounts):
    owner = accounts[0]
    safe = create_simple_safe(local_node_gc_replay.w3, owner)
    assert safe.retrieve_owners() == [owner.address]
