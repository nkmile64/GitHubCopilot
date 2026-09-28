from __future__ import annotations

import argparse

_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_BASE = len(_ALPHABET)


def _validate_base62(value: str) -> str:
    if not value:
        raise ValueError("Base62 value cannot be empty.")
    invalid = next((char for char in value if char not in _ALPHABET), None)
    if invalid is not None:
        raise ValueError(f"Invalid base62 character: {invalid!r}")
    return value


def _encode_int(value: int) -> str:
    if value < 0:
        raise ValueError("Base62 encoding only supports non-negative integers.")
    if value == 0:
        return "0"

    digits: list[str] = []
    while value:
        value, remainder = divmod(value, _BASE)
        digits.append(_ALPHABET[remainder])
    return "".join(reversed(digits))


def _decode_int(value: str) -> int:
    normalized = _validate_base62(value)
    result = 0
    for char in normalized:
        result = result * _BASE + _ALPHABET.index(char)
    return result


def encode(data: str | bytes | bytearray | int) -> str:
    """Encode text, bytes, or a non-negative integer as a base62 string."""
    if isinstance(data, int):
        return _encode_int(data)
    if isinstance(data, str):
        return encode(data.encode("utf-8"))
    if isinstance(data, (bytes, bytearray)):
        raw = bytes(data)
        if not raw:
            return "0:"
        value = int.from_bytes(raw, byteorder="big", signed=False)
        return f"{len(raw)}:{_encode_int(value)}"
    raise TypeError("Unsupported type for base62 encoding. Use int, str, bytes, or bytearray.")


def decode(value: str, *, mode: str = "auto") -> bytes | int:
    """Decode a base62 string.

    By default, plain values decode as integers and length-prefixed payloads
    decode as bytes.
    """
    if mode not in {"auto", "bytes", "int"}:
        raise ValueError("mode must be 'auto', 'bytes', or 'int'.")

    if mode == "int":
        return _decode_int(value)

    if mode == "bytes":
        if ":" not in value:
            raise ValueError("Byte payloads must be encoded with a length prefix such as '5:abc12'.")
        length_text, encoded = value.split(":", 1)
        if not length_text.isdigit():
            raise ValueError("Byte payload length must be a nonnegative integer.")

        length = int(length_text)
        if length == 0:
            if encoded:
                raise ValueError("Empty payload must be encoded as '0:'.")
            return b""

        digits = _validate_base62(encoded)
        integer_value = _decode_int(digits)
        return integer_value.to_bytes(length, byteorder="big", signed=False)

    if ":" in value:
        return decode(value, mode="bytes")
    return _decode_int(value)


def encode_int(value: int) -> str:
    return _encode_int(value)


def decode_int(value: str) -> int:
    return _decode_int(value)


def main() -> None:
    parser = argparse.ArgumentParser(description="Base62 encoder/decoder")
    parser.add_argument("action", choices=["encode", "decode"], help="Operation to perform")
    parser.add_argument("value", help="String, bytes, or integer to encode/decode")
    parser.add_argument("--mode", choices=["auto", "bytes", "int"], default="auto", help="Decode mode")
    args = parser.parse_args()

    if args.action == "encode":
        try:
            number = int(args.value)
            print(encode(number))
        except ValueError:
            print(encode(args.value))
    else:
        result = decode(args.value, mode=args.mode)
        if isinstance(result, bytes):
            print(result.decode("utf-8", errors="surrogateescape"))
        else:
            print(result)
