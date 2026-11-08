"""
place_values.py
---------------

Provides tools for decomposing positive integers into their individual
place-value components.

Classes:
    PlaceValues:
        Represents an integer by breaking it into its thousands, hundreds,
        tens, and units components.
"""

from dataclasses import dataclass


@dataclass
class PlaceValues:
    """
    Represent the digits of a non-negative integer by their place values.

    Numbers are split into thousands, hundreds, tens, and units digits.

    Example:
        >>> value = PlaceValues(1600)
        >>> value.thousands
        1
        >>> value.hundreds
        6
        >>> value.tens
        0
        >>> value.units
        0
        >>> value.decompose()
        [1000, 600, 0, 0]

    Attributes:
        number (int):
            The integer to decompose into place-value digits.

    Properties:
        thousands (int):
            The thousands digit.
        hundreds (int):
            The hundreds digit.
        tens (int):
            The tens digit.
        units (int):
            The units digit.
    """

    number: int

    def __post_init__(self):
        """
        Validate the number after initialization.

        A number is valid if it is NOT negative.

        Raises:
            ValueError:
                If `number` is negative.
        """
        if self.number < 0:
            raise ValueError(f"`number` must not be negative: '{self.number}'")

    @property
    def thousands(self) -> int:
        """
        Return the thousands digit.
        """
        return self.number // 1000 % 10

    @property
    def hundreds(self) -> int:
        """
        Return the hundreds digit.
        """
        return self.number // 100 % 10

    @property
    def tens(self) -> int:
        """
        Return the tens digit.
        """
        return self.number // 10 % 10

    @property
    def units(self) -> int:
        """
        Return the units digit.
        """
        return self.number % 10

    def decompose(self, as_strings: bool=False) -> list[int] | list[str]:
        """
        Break the number into its component parts such that, when added together,
        they reconstruct the original value.

        For example, 2609 decomposes to [2000, 600, 0, 9].

        Example:
            >>> PlaceValues(1600).decompose()
            [1000, 600, 0, 0]
            >>> PlaceValues(1600).decompose(as_strings=True)
            ['1000', '600', '00', '0']

        Args:
            as_strings (bool):
                Whether to return integers or strings. Strings preserve leading
                zeros where needed.

        Returns:
            list[int] | list[str]:
                A list of place-value components, either as integers or strings.
        """
        number_str = str(self.number)
        length = len(number_str)

        l = []

        for i in range(0, length):
            if as_strings:
                _ = (number_str[i].ljust(length-i, '0'))
            else:
                _ = int(number_str[i].ljust(length-i, '0'))
            
            l.append(_)

        return l