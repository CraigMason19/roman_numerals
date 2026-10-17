import unittest

from source.place_values import PlaceValues


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