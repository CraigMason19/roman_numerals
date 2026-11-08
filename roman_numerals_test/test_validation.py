import unittest

from roman_numerals.validation import (
    contains_only_numerals,
    is_mixed_case,
    tokenize,
    _rule_1,
    _rule_2,
    _rule_3,
    _rule_4,
    validate_numeral,
    is_valid,
)

#region General

class TestContainsOnlyNumerals(unittest.TestCase):
    def test_true_input(self):
        inputs = [
            'I',
            'IVXM',
            'vixiiiiiii',
            'XiVMd',
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(contains_only_numerals(value))

    def test_false_input(self):
        inputs = [
            'I I',
            'IK',
            'V7',
            'XVI!',
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertFalse(contains_only_numerals(value))


class TestMixedCase(unittest.TestCase):
    def test_true_input(self):
        inputs = [
            'Vii',
            'Hello World',
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(is_mixed_case(value))

    def test_false_input(self):
        inputs = [
            'HELLO',
            'world123',
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertFalse(contains_only_numerals(value))


class TestTokenize(unittest.TestCase):
    def test_duplicate_subtractive_pairs(self):
        result = tokenize("IXIX")
        expected = ["IX", "IX"]

        self.assertEqual(result, expected)

    def test_numeral_with_decimals(self):
        """
        A common Renaissance style.
        """
        result = tokenize("M.DC.XXIII")
        expected = ['M', 'D', 'C', 'X', 'X', 'I', 'I', 'I']

        self.assertEqual(result, expected)

    def test_numeral_with_spaces(self):
        result = tokenize("M DC XXIII")
        expected = ['M', 'D', 'C', 'X', 'X', 'I', 'I', 'I']

        self.assertEqual(result, expected)

#endregion


# region Rules

class TestRule1(unittest.TestCase):
    def test_same_next_to_passes(self):
        result = _rule_1(['IX', 'IX'])

        self.assertTrue(result)

    def test_lower_next_to_passes(self):
        result = _rule_1(['IX', 'i'])

        self.assertTrue(result)

    def test_higher_next_to_subtractive_pair_fails(self):
        result = _rule_1(['IX', 'X'])

        self.assertFalse(result)

    def test_higher_subtractive_pair_next_to_fails(self):
        result = _rule_1(['I', 'IX'])

        self.assertFalse(result)


class TestRule2(unittest.TestCase):
    def test_too_many_numerals_fails(self):
            inputs = [
                "I" * 16,
                "I" * 10,
                "M" + ("C" * 10)
            ]

            for value in inputs:
                with self.subTest(value=value):
                    self.assertFalse(_rule_2(value))

    def test_ftoo_many_numerals_fails(self):
            inputs = [
                "I" * 9,
                "M" + ("C" * 9)
            ]

            for value in inputs:
                with self.subTest(value=value):
                    self.assertTrue(_rule_2(value))


class TestRule3(unittest.TestCase):
    def test_no_numeral_true(self):
        inputs = [
            [''],
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(_rule_3(value))

    def test_one_numeral_true(self):
        inputs = [
            ['D'],
            ['L'],
            ['V'],
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(_rule_3(value))

    def test_more_than_one_numeral_false(self):
        inputs = [
            ['D', 'D'],
            ['L', 'L'],
            ['V', 'V'],
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertFalse(_rule_3(value))


class TestRule4(unittest.TestCase):
    def test_multiple_different_pairs_true(self):
        inputs = [
            ['CM', 'IX', 'IV'],
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(_rule_4(value))

    def test_multiple_same_pairs_false(self):
        inputs = [
            ['CM', 'IV', 'IV'],
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertFalse(_rule_4(value))

#endregion


#region Validity

class TestValidateNumeral(unittest.TestCase):
    def test_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            validate_numeral("")

    def test_spaces_raises_value_error(self):
        with self.assertRaises(ValueError):
            validate_numeral("VII I")

    def test_invalid_characters_raises_value_error(self):
        with self.assertRaises(ValueError):
            validate_numeral("IK")

    def test_mixed_case_raises_value_error(self):
        with self.assertRaises(ValueError):
            validate_numeral("Vi")

    def test_rule_1_is_applied(self):
        with self.assertRaises(ValueError):
            validate_numeral("IXX") 

    def test_rule_2_is_applied(self):
        with self.assertRaises(ValueError):
            validate_numeral("X" + ("I" * 10)) 

    def test_rule_3_is_applied(self):
        with self.assertRaises(ValueError):
            validate_numeral("DDI")      

    def test_rule_4_is_applied(self):
        with self.assertRaises(ValueError):
            validate_numeral("IXIX")    


class TestIsValid(unittest.TestCase):
    def test_empty_string_false(self):
        result = is_valid("")

        self.assertFalse(result) 

    def test_lowercase_true(self):
        result = is_valid("xcix")

        self.assertTrue(result) 

    def test_uppercase_true(self):
        result = is_valid("XCIX")

        self.assertTrue(result) 

    def test_mixed_case_false(self):
        result = is_valid("XCiX")
        
        self.assertFalse(result) 

    def test_numbers_false(self):
        result = is_valid("X5")
        
        self.assertFalse(result) 

#endregion


#region Euler Note Examples

class Test_16(unittest.TestCase):
    def test_valid(self):
        inputs = [
            "XVI",
            "XIIIIII",
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(is_valid(value))

    def test_invalid(self):
        inputs = [
            "I" * 16,
            "I" * 10,
            "VVVI",
            "VVIIIIII",
            "VIIIIIIIIIII",
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertFalse(is_valid(value))


class Test_49(unittest.TestCase):
    def test_valid(self):
        inputs = [
            "XXXXIIIIIIIII",
            "XXXXVIIII",
            "XXXXIX",
            "XLIIIIIIIII",
            "XLVIIII",
            "XLIX",
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(is_valid(value))

    def test_invalid(self):
        result = is_valid("IL")

        self.assertFalse(result) 
  

class Test_1606(unittest.TestCase):
    def test_valid(self):
        inputs = [
            "MCCCCCCVI",
            "MDCVI"
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(is_valid(value))     


class Test_verbose(unittest.TestCase):
    def test_valid(self):
        inputs = [
            "IIIII",
            "V",
            "XXXXX",
            "D",
            "CCCCC",
            "M"
        ]

        for value in inputs:
            with self.subTest(value=value):
                self.assertTrue(is_valid(value))  

#endregion