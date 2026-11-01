NUMERAL_LOOKUP = { 
    'I': 1,    'i': 1, 
    'V': 5,    'v': 5,
    'X': 10,   'x': 10,
    'L': 50,   'l': 50, 
    'C': 100,  'c': 100,
    'D': 500,  'd': 500,
    'M': 1000, 'm': 1000,
}

SUBTRACTIVE_PAIRS_LOOKUP = {
    "IV": 5,   "iv": 5, 
    "IX": 9,   "ix": 9,
    "XL": 40,  "xl": 40, 
    "XC": 90,  "xc": 90, 
    "CD": 400, "cd": 400,
}


def contains_only_numerals(s: str) -> bool:
    """
    Returns True if ALL characters in a string contain valid numeral characters,
    False otherwise. 
    
    Case is ignored.

    Example:
        >>> contains_only_numerals("XiVmD")
        True
        >>> contains_only_numerals("XiV mD")
        False

    Args:
        s (str):

    Returns:
        bool:
    """
    return all(_ in NUMERAL_LOOKUP for _ in s)


def is_mixed_case(s: str) -> bool:
    """
    Returns `True` if a string uses lower and upper case characters, `False` 
    otherwise.

    Example:
        >>> is_mixed_case("Hello")
        True
        >>> is_mixed_case("HELLO")
        False

    Args:
        s (str):

    Returns:
        bool
    """
    return s.islower() is False and s.isupper() is False and s.lower() != s.upper()



    

def tokenize(numeral_str: str) -> list[str]:
    """
    Splits a string of numerals into UPPERCASE tokens which are either a numeral, or a pair of subtractive numerals.

    Args:
        numeral_str (str):
            A string containing ONLY roman numerals.

    Examples:
        >>> tokenize("IXX")
        ['IX', 'X']

        >>> tokenize("XIX")
        ['X', 'IX']

        >>> tokenize("XXI")
        ['X', 'X', 'I']

        >>> tokenize("XIXIX")
        ['X', 'IX', 'IX']

    Returns:
        list[str]:
            A list of uppercase tokens.
    """
    line = numeral_str.upper() # So we don't have 'iX' for example
    parts = []
    
    while len(line) > 0:
        if line[0:2] in SUBTRACTIVE_PAIRS_LOOKUP:
            parts.append(line[0:2])
            line = line[2:]

        elif line[0] in NUMERAL_LOOKUP:
            parts.append(line[0])
            line = line[1:]

    return parts




 




def validate_numeral(s: str) -> None:
    if s == "":
        raise ValueError(f"Numeral string is empty: '{s}'")

    if not contains_only_numerals(s):
        raise ValueError(f"Contains characters other than numerals: '{s}'")

    if is_mixed_case(s):
        raise ValueError(f"Numerals must be of the same case: '{s}'")



    # etc.......





def is_valid(s: str) -> bool:
    """
    Determines is a string is a valid roman numeral.

    Args:
        s (str):

    Returns:
        bool
    """
    try:
        validate_numeral(s)
        return True
    
    except ValueError:
        return False