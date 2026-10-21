"""
roman_numerals.py
---------------

Provides tools for constructing / displaying Roman numerals.

Globals:
    NUMERAL_LOOKUP (dict[str, int]):
        A dictionary mapping Roman numeral characters (uppercase and lowercase) 
        to their corresponding numeric values.

Classes:
    Numeral: 
        Represents an Roman numeral.

Functions:
    print_numeral_details:
        Conveniently display a Numeral and all its various properties.
"""

from typing import Self

from roman_numerals.place_values import PlaceValues


NUMERAL_LOOKUP = { 
    'I': 1, 'i': 1, 
    'V':5, 'v':5,
    'X':10, 'x':10,
    'L':50, 'l':50, 
    'C':100, 'c':100,
    'D':500, 'd':500,
    'M':1000, 'm':1000,
}


class Numeral:
    """
    Represents a Roman numeral in between 1 -> 9,999 (inclusive).

    Example:
        >>> n = Numeral("XIIII")
        >>> n.str
        "XIIII"
        >>> n.value
        14
        >>> n.minimal_str
        "XIV"
        >>> n.minimal_saving
        2
        >>> n.uses_subtractive_pair_rule
        False

        >>> Numeral.from_int(14)
        'Numeral("XIV")'

    Attributes:
        str (str):
            The original str passed to the Numeral's constructor.
        value (int):
            The numerical value of the Numeral.
        minimal_str (str):
            The Numeral expressed in it's minimal form.

    Properties:
        minimal_saving (int):
            The difference between `str` & `minimal_str`.
    """

    def __init__(self, numeral_str : str):
        """
        Constructs a Numeral class is the `numeral_str` is a valid numeral string.

        Args:
            numeral_str (str):
                The string to try to make a Numeral from.

        Raises:
            ValueError:
                If the Numeral is invalid. As determined by the `is_valid` method.
        """
        if not Numeral.is_valid(numeral_str):
            raise ValueError(f"`numeral_str` contains an invalid denomination. '{numeral_str}'")
        
        self.str = numeral_str.upper()
        self.value = self._calculate_value(self.str)
        self.minimal_str = self._calculate_minimal_numeral(self.value)

    @property
    def minimal_saving(self) -> int:
        """
        A property that returns the difference between the `str` and 
        `minimal_str` instance attributes.

        Returns:
            int
        """
        return len(self.str) - len(self.minimal_str)
    
    def __eq__(self, other: Self) -> bool:
        """
        Compares if a numeral is equal to another based upon it's numerical value. 
        This allows you to compare numeral `str` and `minimal_str`. 

        Example:
            >>> Numeral("VIIII") == Numeral("IX") == Numeral.from_int(9)
            True

        Args:
            other (Numeral):
                Another Numeral object to compare

        Returns:
            bool
        """
        if not isinstance(other, Numeral):
            return NotImplemented

        return self.value == other.value
    
    @staticmethod
    def is_valid(numeral_str : str) -> bool:
        """
        """
        if numeral_str == "":
            return False

        for n in numeral_str:
            if n not in NUMERAL_LOOKUP:
                return False

        return True

    @staticmethod
    def uses_subtractive_pair_rule(numeral_str : str) -> bool:
        """
        Example:
            >>> Numeral.uses_subtractive_pair_rule("IX")
            True

        Returns:
            bool
        """
        for i in range(1, len(numeral_str)):
            if NUMERAL_LOOKUP[numeral_str[i]] > NUMERAL_LOOKUP[numeral_str[i-1]]:
                return True
            
        return False
    
    @staticmethod
    def from_int(n: int) -> Self:
        """
        Creates a Roman numeral from a number. 
        
        - Limit is 1 -> 9,999 (inclusive). 0 had no a Roman numeral.
        - Numerals created this way will use the minimal form of the numeral

        Args:
            n (int): 
                A positive integer to convert.

        Raises:
            ValueError:
                If `n` isn't a positive integer. 
        """
        if n < 1:
            raise ValueError(f"`n` must be a positive integer: {n}")

        minimal_str = Numeral._calculate_minimal_numeral(n)
        return Numeral(minimal_str)


    @staticmethod
    def _calculate_minimal_numeral(value) -> str:
        """
        # Works bellow 10,000 (V with overscore).
        """
        number_str = str(value)
        length = len(number_str)
        
        # 1600 -> [1000, 600, 00, 0]
        l = PlaceValues(value).decompose(as_strings=True)

        numeral = ''
        for item in l:
            if item[0] != '0':
                # Determine digits, tens, hundreds, thousands
                length = len(item)

                if length == 1:
                    small, mid, big = 'I', 'V', 'X'
                if length == 2:
                    small, mid, big = 'X', 'L', 'C'
                if length == 3:
                    small, mid, big = 'C', 'D', 'M'
                if length == 4:
                    numeral += 'M' * int(item[0])
                    continue

                n = int(item[0])
                if n == 1:
                    numeral += small
                if n == 2:
                    numeral += small+small
                if n == 3:
                    numeral += small+small+small
                if n == 4:
                    numeral += small+mid
                if n == 5:
                    numeral += mid
                if n == 6:
                    numeral += mid+small
                if n == 7:
                    numeral += mid+small+small
                if n == 8:
                    numeral += mid+small+small+small
                if n == 9:
                    numeral += small+big

        return numeral

    @staticmethod
    def _calculate_value(numeral_str: str) -> int:
        if Numeral.uses_subtractive_pair_rule(numeral_str) == False:
            return sum(NUMERAL_LOOKUP[c] for c in numeral_str)
        
        else:
            total = 0
            for i in range(0, len(numeral_str)-1):
                if NUMERAL_LOOKUP[numeral_str[i]] < NUMERAL_LOOKUP[numeral_str[i+1]]:
                    total -= NUMERAL_LOOKUP[numeral_str[i]]
                else:
                    total += NUMERAL_LOOKUP[numeral_str[i]]

        return total + int(NUMERAL_LOOKUP[numeral_str[-1:]])

    def __str__(self) -> str:
        """
        Displays the numeral using the `str` instance attribute.

        Example:
            >>> n = Numeral("MDCCCXLIX")
            >>> str(n)
            "MDCCCXLIX"

        Returns:
            str
        """
        return f"{self.str}"
    
    def __repr__(self) -> str:
        """
        Displays the numeral using the `str` instance attribute.

        Example:
            >>> n = Numeral("MDCCCXLIX")
            >>> repr(n)
            "Numeral('MDCCCXLIX')"

        Returns:
            str
        """
        return f'Numeral("{self.str}")'


def print_numeral_details(numeral: Numeral) -> None: # pragma: no cover
    """
    Prints the numeral's full details for useful display / debugging

    Example:
        >>> print_numeral_details(Numeral("XIIII"))
        Numeral("XIIII")
            str -> "XIIII"
            value -> 14
            minimal_str -> "XIV"
            minimal_saving -> 2
            uses_subtractive_pair_rule -> False

    Args:
        numeral (Numeral):
            The Numeral you wish to display.
    """
    print(repr(numeral))
    print(f'\tstr -> "{numeral.str}"')
    print(f"\tvalue -> {numeral.value}")
    print(f'\tminimal_str -> "{numeral.minimal_str}"')
    print(f"\tminimal_saving -> {numeral.minimal_saving}")
    print(f"\tuses_subtractive_pair_rule -> {numeral.uses_subtractive_pair_rule(numeral.str)}")