"""
roman_numerals
---------------

Provides tools & utilities for working with Roman numerals.

Modules:
    place_values:
        Defines the `PlaceValues` helper for decomposing integers by place value.

    roman_numerals:
        Defines the tools for creating and displaying Roman numerals.

    validation:
        Defines the tools for validating Roman numeral strings.
"""

from .place_values import PlaceValues
from .roman_numerals import Numeral, print_numeral_details
from .validation import validate_numeral