import unittest

from roman_numerals.place_values import PlaceValues


class TestPlaceValuesConstruction(unittest.TestCase):
    def test_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = PlaceValues(-1)

    def test_0_construction_doesnt_raise_error(self):
        try:
            _ = PlaceValues(0)
        except Exception as e: # pragma: no cover
            self.fail(f"Raised an exception: {e}")


class TestPlaceValuesAttributes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.place_values = PlaceValues(1623)

    def test_thousands(self):
        result = self.place_values.thousands
        expected = 1

        self.assertEqual(result, expected)

    def test_hundreds(self):
        result = self.place_values.hundreds
        expected = 6

        self.assertEqual(result, expected)

    def test_tens(self):
        result = self.place_values.tens
        expected = 2

        self.assertEqual(result, expected)

    def test_units(self):
        result = self.place_values.units
        expected = 3

        self.assertEqual(result, expected)


class TestPlaceValuesDecompose(unittest.TestCase):
    def test_returns_list(self):
        result = PlaceValues(1609).decompose()
        
        self.assertIsInstance(result, list)

    def test_returns_list_of_int(self):
        result = PlaceValues(1609).decompose(as_strings=False)

        for _ in result:
            self.assertIsInstance(_, int)

    def test_returns_list_of_str(self):
        result = PlaceValues(1609).decompose(as_strings=True)

        for _ in result:
            self.assertIsInstance(_, str)

    def test_99_999_decomposes_correctly(self):
        result = PlaceValues(99_999).decompose()
        expected = [90000, 9000, 900, 90, 9]

        self.assertEqual(result, expected)

    def test_as_strings_false(self):
        result = PlaceValues(1609).decompose()
        expected = [1000, 600, 0, 9]

        self.assertEqual(result, expected)

    def test_as_strings_true(self):
        result = PlaceValues(1609).decompose(as_strings=True)
        expected = ['1000', '600', '00', '9']

        self.assertEqual(result, expected)