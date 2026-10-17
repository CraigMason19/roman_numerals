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

    def __init__(self, number):
        """
        Protects against negative number construction.

        Args:
            number (int):
                A positive integer of the number to represent.

        Raises:
            ValueError:
                If `number` is negative.
        """
        if number < 0:
            raise ValueError(f"`number` must be a positive integer: '{number}'")

        self.number = number

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
        Breaks the number into component parts such that when added together
        re-construct the original number. For example,

        2609 decomposed becomes [2000, 600, 0, 9]. The sum of which is 2609.

        Example:
            >>> PlaceValues(1600).decompose()
            [1000, 600, 0, 0]
            >>> PlaceValues(1600).decompose(as_strings=True)
            ['1000', '600', '00', '9']

        Args:
            as_strings (bool):
                Whether or not the method should return ints or strings. This 
                allows for leading zeros.

        Returns:
            list[int] | list[str]:
                Either a list of ints or a list of strings depending on `as_strings`
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