

from typing import Self


NUMERALS = { 
    'I': 1, 'i': 1, 
    'V':5, 'v':5,
    'X':10, 'x':10,
    'L':50, 'l':50, 
    'C':100, 'c':100,
    'D':500, 'd':500,
    'M':1000, 'm':1000,
}


# @dataclass
# class Units:
#     thousands


class Numeral:
    """
    1 to 9,999
    """

    def __init__(self, numeral_str : str):
        if not Numeral.is_valid(numeral_str):
            raise ValueError(f"`numeral_str` contains an invalid denomination. '{numeral_str}'")
        
        self.str = numeral_str.upper()
        self.value = self._calculate_value(self.str)
        self.minimal_str = self._calculate_minimal_numeral(self.value)

    @staticmethod
    def is_valid(numeral_str : str) -> bool:
        for n in numeral_str:
            if n not in NUMERALS:
                return False

        return True

    @staticmethod
    def uses_subtractive_pair_rule(numeral_str : str) -> bool:
        """
            # e.g. IX, XC
        """
        for i in range(1, len(numeral_str)):
            if NUMERALS[numeral_str[i]] > NUMERALS[numeral_str[i-1]]:
                return True
            
        return False
    
    @staticmethod
    def from_int(n: int) -> Self:
        """
        Creates a roman numeral from a number. Limit 5000

        Args:
            n (int): 
                The integer to convert. Must be a positive integer.

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
        # print(number_str)
        length = len(number_str)
        
        # 1600 -> [1000, 600, 00, 0]
        l = [number_str[i].ljust(length-i, '0') for i in range(0, length)]
        # print(l)

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
            return sum(NUMERALS[c] for c in numeral_str)
        
        else:
            total = 0
            for i in range(0, len(numeral_str)-1):
                if NUMERALS[numeral_str[i]] < NUMERALS[numeral_str[i+1]]:
                    total -= NUMERALS[numeral_str[i]]
                else:
                    total += NUMERALS[numeral_str[i]]

        return total + int(NUMERALS[numeral_str[-1:]])


    
    def __repr__(self) -> str:
        return f"Numeral('{self.str}')"






 


def print_numeral_details(numeral: Numeral) -> None:
    """
    Prints the numeral's ful
    """
    print(numeral)
    print(numeral.str)
    print(numeral.value)
    print(numeral.minimal_str)
    print(Numeral.uses_subtractive_pair_rule(numeral.str))


numerals = [
    "MMDCCLXXXVIIII",
]

# print_numeral_details(Numeral('MMMMCCCXLIV'))
# print()
# print_numeral_details(Numeral.from_int(0))
# print_numeral_details(Numeral.from_int(9999))
# print_numeral_details(Numeral.from_int(10_000))
