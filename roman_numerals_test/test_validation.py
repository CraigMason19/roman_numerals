import unittest

from roman_numerals.validation import (
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