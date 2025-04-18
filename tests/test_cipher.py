import unittest
from cipher import decrypt_caesar

class TestCipher(unittest.TestCase):
    def test_basic_shift(self):
        self.assertEqual(decrypt_caesar("ifmmp", 1), "hello")
    def test_wrap_around(self):
        self.assertEqual(decrypt_caesar("abc", 2), "cde")

if __name__ == "__main__":
    unittest.main()