"""
roman_numerals.py
-----------------

Provides tools for constructing and displaying Roman numerals.

Classes:
    Numeral:
        Represents a Roman numeral between 1 and 9,999 inclusive.

Functions:
    print_numeral_details:
        Prints a numeral and its associated properties in a readable format.
"""

from typing import Self

from roman_numerals.place_values import PlaceValues
from roman_numerals.validation import NUMERAL_VALUE_LOOKUP, SUBTRACTIVE_PAIRS_VALUE_LOOKUP, is_valid


class Numeral:
    """
    Represents a Roman numeral in the range 1 to 9,999 inclusive.

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
            The original string passed to the constructor.
        value (int):
            The integer value represented by the numeral.
        minimal_str (str):
            The numeral expressed in its shortest valid form.

    Properties:
        minimal_saving (int):
            The number of characters saved by converting `str` to `minimal_str`.
    """

    def __init__(self, numeral_str: str):
        """
        Create a `Numeral` from a valid Roman numeral string.

        Args:
            numeral_str (str):
                The Roman numeral string to validate and parse.

        Raises:
            ValueError:
                If the supplied string is not a valid numeral.
        """
        if not Numeral.is_valid(numeral_str):
            raise ValueError(f"`numeral_str` contains an invalid denomination. '{numeral_str}'")

        self.str = numeral_str.upper()
        self.value = self._calculate_value(self.str)
        self.minimal_str = self._calculate_minimal_numeral(self.value)

    @property
    def minimal_saving(self) -> int:
        """
        Return the difference in length between the original string and its minimal form.

        Returns:
            int
        """
        return len(self.str) - len(self.minimal_str)

    def __eq__(self, other: Self) -> bool:
        """
        Compare two numerals by their numeric value.

        This also allows direct comparisons between a numeral's original form and
        its minimal representation.

        Example:
            >>> Numeral("VIIII") == Numeral("IX") == Numeral.from_int(9)
            True

        Args:
            other (Numeral):
                Another `Numeral` instance to compare against.

        Returns:
            bool
        """
        if not isinstance(other, Numeral):
            return NotImplemented

        return self.value == other.value

    @staticmethod
    def is_valid(text: str) -> bool:
        """
        Return whether the provided text is a valid Roman numeral.

        Args:
            text (str):
                The string to validate.

        Returns:
            bool:
        """
        return is_valid(text)

    @staticmethod
    def uses_subtractive_pair_rule(numeral_str: str) -> bool:
        """
        Determine whether the numeral uses a subtractive pair rule.

        The method inspects adjacent characters and checks whether a smaller value
        appears before a larger one, which indicates a subtractive notation such
        as `IV` or `IX`.

        Example:
            >>> Numeral.uses_subtractive_pair_rule("XIX")
            True

        Returns:
            bool
        """
        for i in range(1, len(numeral_str)):
            if NUMERAL_VALUE_LOOKUP[numeral_str[i]] > NUMERAL_VALUE_LOOKUP[numeral_str[i-1]]:
                return True

        return False

    @staticmethod
    def from_int(n: int) -> Self:
        """
        Create a Roman numeral from a positive integer.

        The result is always expressed in its minimal valid form.

        Args:
            n (int):
                A positive integer to convert.

        Raises:
            ValueError:
                If `n` is not a positive integer.
        """
        if n < 1:
            raise ValueError(f"`n` must be a positive integer: {n}")

        minimal_str = Numeral._calculate_minimal_numeral(n)
        return Numeral(minimal_str)

    @staticmethod
    def _calculate_minimal_numeral(value: int) -> str:
        """
        Compute the minimal Roman numeral representation for an integer below 10,000.
        
        Example:
            >>> Numeral._calculate_minimal_numeral(14)
            "XIV"

        Args:
            value:
                The integer to represent as a Roman numeral.

        Returns:
            str: 
                The minimal Roman numeral representation of the integer.
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
                    numeral += small + small
                if n == 3:
                    numeral += small + small + small
                if n == 4:
                    numeral += small + mid
                if n == 5:
                    numeral += mid
                if n == 6:
                    numeral += mid + small
                if n == 7:
                    numeral += mid + small + small
                if n == 8:
                    numeral += mid + small + small + small
                if n == 9:
                    numeral += small + big

        return numeral

    @staticmethod
    def _calculate_value(numeral_str: str) -> int:
        """
        Compute the integer value of a Roman numeral string.
        
        Example:
            >>> Numeral._calculate_value("XIV") 
            14

        Args:
            numeral_str (str):
                The Roman numeral string to evaluate.

        Returns:
            int:
                The integer value of the numeral.        
        """
        if Numeral.uses_subtractive_pair_rule(numeral_str) == False:
            return sum(NUMERAL_VALUE_LOOKUP[c] for c in numeral_str)

        else:
            total = 0
            for i in range(0, len(numeral_str)-1):
                if NUMERAL_VALUE_LOOKUP[numeral_str[i]] < NUMERAL_VALUE_LOOKUP[numeral_str[i+1]]:
                    total -= NUMERAL_VALUE_LOOKUP[numeral_str[i]]
                else:
                    total += NUMERAL_VALUE_LOOKUP[numeral_str[i]]

        return total + int(NUMERAL_VALUE_LOOKUP[numeral_str[-1:]])

    def pretty_print(self) -> None: # pragma: no cover
        """
        Print the numeral and its details using `print_numeral_details`.
        """
        print_numeral_details(self)

    def __str__(self) -> str:
        """
        Return the numeral using the original string representation.

        Example:
            >>> n = Numeral("MDCCCXLIX")
            >>> str(n)
            "MDCCCXLIX"

        Returns:
            str: 
                The original numeral string.
        """
        return f"{self.str}"

    def __repr__(self) -> str:
        """
        Return a developer-friendly representation of the numeral.

        Example:
            >>> n = Numeral("MDCCCXLIX")
            >>> repr(n)
            "Numeral('MDCCCXLIX')"

        Returns:
            str: 
                The numeral's representation.
        """
        return f'Numeral("{self.str}")'


def print_numeral_details(numeral: Numeral) -> None: # pragma: no cover
    """
    Print the numeral and each of its key properties for display or debugging.

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
            The Numeral to display.
    """
    print(repr(numeral))
    print(f'\tstr -> "{numeral.str}"')
    print(f"\tvalue -> {numeral.value}")
    print(f'\tminimal_str -> "{numeral.minimal_str}"')
    print(f"\tminimal_saving -> {numeral.minimal_saving}")
    print(f"\tuses_subtractive_pair_rule -> {numeral.uses_subtractive_pair_rule(numeral.str)}")