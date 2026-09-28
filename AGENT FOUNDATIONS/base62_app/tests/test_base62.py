import unittest

from base62_app import decode, encode


class Base62Tests(unittest.TestCase):
    def test_encode_decode_round_trip_for_text(self):
        original = "hello, world!"
        encoded = encode(original)
        self.assertIsInstance(encoded, str)
        self.assertEqual(decode(encoded), original.encode("utf-8"))

    def test_encode_decode_round_trip_for_bytes(self):
        original = b"\x00\x01\x02\x03\xff\xff"
        encoded = encode(original)
        self.assertEqual(decode(encoded), original)

    def test_integer_round_trip(self):
        self.assertEqual(encode(0), "0")
        self.assertEqual(encode(1), "1")
        self.assertEqual(encode(62), "10")
        self.assertEqual(encode(123456), "w7e")
        self.assertEqual(decode("w7e"), 123456)

    def test_invalid_characters_are_rejected(self):
        with self.assertRaises(ValueError):
            decode("hello-World")


if __name__ == "__main__":
    unittest.main()
