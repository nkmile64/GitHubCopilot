import pytest

from app import base62


@pytest.mark.parametrize("n", [0, 1, 61, 62, 63, 3844, 10**12, 2**63 - 1])
def test_round_trip(n):
    assert base62.decode(base62.encode(n)) == n


def test_known_values():
    assert base62.encode(0) == "0"
    assert base62.encode(61) == "Z"
    assert base62.encode(62) == "10"


def test_decode_invalid():
    with pytest.raises(ValueError):
        base62.decode("ab-c")
    with pytest.raises(ValueError):
        base62.decode("")


def test_encode_negative():
    with pytest.raises(ValueError):
        base62.encode(-1)
