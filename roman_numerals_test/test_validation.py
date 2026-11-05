import unittest

from roman_numerals.validation import (
    tokenize,
    _rule_1,
    validate_numeral,
    is_valid,
)



class TestValidation(unittest.TestCase):
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




# class TestIsValid(unittest.TestCase):
#     def test_empty_string_false(self):
#         result = is_valid("")
#         expected = False

#         self.assertEqual(result, expected) 

#     def test_lowercase_true(self):
#         result = is_valid("xcix")
#         expected = True

#         self.assertEqual(result, expected) 

#     def test_uppercase_true(self):
#         result = is_valid("XCIX")
#         expected = True

#         self.assertEqual(result, expected) 

#     def test_mixed_case_false(self):
#         result = is_valid("XCIX")
#         expected = True

#         self.assertEqual(result, expected) 