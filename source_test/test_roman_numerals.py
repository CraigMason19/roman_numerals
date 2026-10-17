import unittest

from source.roman_numerals import Numeral, NUMERALS


class TestNumeral(unittest.TestCase):
    def test_empty_string_is_invalid(self):
        with self.assertRaises(ValueError):
            _ = Numeral("0")

    def test_0_is_invalid(self):
        with self.assertRaises(ValueError):
            _ = Numeral.from_int(0)
