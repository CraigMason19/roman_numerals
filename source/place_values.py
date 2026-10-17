from dataclasses import dataclass

@dataclass
class PlaceValues:
    """
    Represent the digits of an integer by their place values.

    Extracts the thousands, hundreds, tens, and units digits
    from a given integer.

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

    Attributes:
        number (int): 
            The integer to decompose into place-value digits.
    """

    number: int

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