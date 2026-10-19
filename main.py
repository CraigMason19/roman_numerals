import os
from random import choice

from source.roman_numerals import Numeral, print_numeral_details

NUMERAL_FILE = "\\resources\\1000_unminimalised_roman_numerals.txt"

def random_numerals(count: int) -> None:
    """
    Loads numeral strings from a file, then chooses `count` many random numerals
    to display. 
    """
    numeral_filename = os.path.dirname(__file__) + NUMERAL_FILE

    with open(numeral_filename) as f:
        lines = f.read().splitlines()

    random_numerals = [choice(lines) for _ in range(count)]

    for n in random_numerals:
        print_numeral_details(Numeral(n))
        print()


if __name__ == "__main__":
    random_numerals(2)