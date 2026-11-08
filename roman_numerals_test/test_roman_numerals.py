import unittest

from roman_numerals.roman_numerals import Numeral, NUMERAL_VALUE_LOOKUP


class TestNumeral(unittest.TestCase):
    def test_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Numeral("")

    def test_invalid_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Numeral("Inv") 

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Numeral.from_int(0)


class TestNumeralMinimalSavingProperty(unittest.TestCase):
    def test_minimal_saving_2(self):
        result = Numeral('MXVIIII').minimal_saving
        expected = 3

        self.assertEqual(result, expected) 


class TestNumeralEQ(unittest.TestCase):
    def test_eq_not_a_numeral(self):
        result = Numeral('VIIII') == int(5)
        expected = False

        self.assertEqual(result, expected)

    def test_numeral_minimal_eq_true(self):
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


class TestNumeralIsValid(unittest.TestCase):
    def test_is_valid_empty_string_false(self):
        result = Numeral.is_valid('')
        expected = False

        self.assertEqual(result, expected)

    def test_is_valid_incorrect_numeral(self):
        result = Numeral.is_valid('G')
        expected = False

        self.assertEqual(result, expected)


class TestNumeralUsesSubtractivePairRule(unittest.TestCase):
    def test_subtractive_pair_true(self):
        result = Numeral.uses_subtractive_pair_rule('XIX')

        self.assertTrue(result)

    def test_subtractive_pair_false(self):
        result = Numeral.uses_subtractive_pair_rule('XVI')

        self.assertFalse(result)


class TestNumeralFromInt(unittest.TestCase):
    def test_from_int_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = Numeral.from_int(0)

    # print_numeral_details(Numeral.from_int(9999))
    # print_numeral_details(Numeral.from_int(10_000))

    def test_from_int_uses_minimal_form_true(self):
        result = str(Numeral.from_int(14))
        expected = "XIV"

        self.assertEqual(result, expected)


class TestNumeralCalculateMinimalNumeral(unittest.TestCase):
    def test_calculate_minimal_numeral_14(self):
        result = Numeral._calculate_minimal_numeral(14)
        expected = "XIV"

        self.assertEqual(result, expected)

    def test_valid_to_minial_numeral_saving(self):
        result = Numeral('MXVIIII').minimal_saving
        expected = 3

        self.assertEqual(result, expected)


class TestNumeralCalculateValue(unittest.TestCase):
    def test_additive_value(self):
        result = Numeral._calculate_value('XVI')
        expected = 16

        self.assertEqual(result, expected)

    def test_subtractive_value(self):
        result = Numeral._calculate_value('XIV')
        expected = 14

        self.assertEqual(result, expected)


class TestNumeralStringRepresentation(unittest.TestCase):
    def test_numeral_str(self):
        result = str(Numeral("MDCCCLXVII"))
        expected = "MDCCCLXVII"

        self.assertEqual(result, expected)

    def test_numeral_repr(self):
        result = repr(Numeral.from_int(1867))
        expected = 'Numeral("MDCCCLXVII")'

        self.assertEqual(result, expected)