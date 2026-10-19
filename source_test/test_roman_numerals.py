import unittest

from source.roman_numerals import Numeral, NUMERALS


class TestNumeral(unittest.TestCase):
    def test_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Numeral("0")

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Numeral.from_int(0)


class TestNumeralEQ(unittest.TestCase):
    def test_numeral_minimal__eq_true(self):
        result = Numeral('VIIII') == Numeral('IX')
        expected = True

        self.assertEqual(result, expected)

    def test_numeral_minimal_eq_false(self):
        result = Numeral('VIIII') == Numeral('IXI')
        expected = False

        self.assertEqual(result, expected)

    def test_numeral_from_int_eq_false(self):
        result = Numeral('VIIII') == Numeral.from_int(10)
        expected = False

        self.assertEqual(result, expected)

    def test_numeral_minimal_from_int_eq_true(self):
        result = Numeral('VIIII') == Numeral('IX') == Numeral.from_int(9)
        expected = True

        self.assertEqual(result, expected)


class TestNumeralFromInt(unittest.TestCase):
    def test_from_int_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Numeral.from_int(0)


# print_numeral_details(Numeral.from_int(9999))
# print_numeral_details(Numeral.from_int(10_000))
