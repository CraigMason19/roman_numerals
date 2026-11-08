"""
validation.py
-------------

Globals:
    NUMERAL_ORDER (list[str]):
        The order of numerals for largest to smallest

    NUMERAL_VALUE_LOOKUP (dict[str, int]):
        A dictionary mapping Roman numeral characters (uppercase and lowercase) 
        to their corresponding numeric values.
        
    SUBTRACTIVE_PAIRS_VALUE_LOOKUP (dict[str, int]):
        A dictionary mapping Roman numeral pairs (uppercase and lowercase) 
        to their corresponding numeric values.

    COMBINED_VALUE_LOOKUP (dict[str, int]):
        A dictionary combining `NUMERAL_VALUE_LOOKUP` & `SUBTRACTIVE_PAIRS_VALUE_LOOKUP`.
"""
from typing import Counter


NUMERAL_ORDER: list[str] = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

NUMERAL_VALUE_LOOKUP: dict[str, int] = { 
    'I': 1,    'i': 1, 
    'V': 5,    'v': 5,
    'X': 10,   'x': 10,
    'L': 50,   'l': 50, 
    'C': 100,  'c': 100,
    'D': 500,  'd': 500,
    'M': 1000, 'm': 1000,
}

SUBTRACTIVE_PAIRS_VALUE_LOOKUP: dict[str, int] = {
    "IV": 5,   "iv": 5, 
    "IX": 9,   "ix": 9,
    "XL": 40,  "xl": 40, 
    "XC": 90,  "xc": 90, 
    "CD": 400, "cd": 400,
    "CM": 900, "cm": 900,
}

COMBINED_VALUE_LOOKUP = NUMERAL_VALUE_LOOKUP | SUBTRACTIVE_PAIRS_VALUE_LOOKUP


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
    return all(_ in NUMERAL_VALUE_LOOKUP for _ in s)


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
    Splits a string of numerals into UPPERCASE tokens which are either a numeral, or
    a pair of subtractive numerals, anything else is discarded.

    DOESN'T check for validity. For Example, "IXIX" becomes ["IX", "IX"].

    Examples:
        >>> tokenize("IXX")
        ['IX', 'X']

        >>> tokenize("XIX")
        ['X', 'IX']

        >>> tokenize("XXI")
        ['X', 'X', 'I']

        >>> tokenize("XIXIX")
        ['X', 'IX', 'IX']

        >>> tokenize("m.dc.xi")
        ['M', 'D', 'C', 'X', 'I']

    Args:
        numeral_str (str):
            The string to split into numerals

    Returns:
        list[str]:
            A list of uppercase tokens.
    """
    line = numeral_str.upper() # So we don't have 'iX' for example
    tokens = []
    
    while len(line) > 0:
        if line[0:2] in SUBTRACTIVE_PAIRS_VALUE_LOOKUP:
            tokens.append(line[0:2])
            line = line[2:]

        elif line[0] in NUMERAL_VALUE_LOOKUP:
            tokens.append(line[0])
            line = line[1:]

        else:
            line = line[1:]

    return tokens


#region Rules

def _rule_1(tokens: list[str]) -> bool:
    """
    Numerals must be arranged in descending order of size.

    Examples:
        >>> _rule_1(['IV', 'I'])
        True
        >>> _rule_1(['IX', 'X'])
        False
    
    Args:
        tokens (list[str]):
            The list of tokens returned by the `tokenize` method.
        
    Returns:
        bool    
    """
    for i in range(len(tokens)-1):
        if COMBINED_VALUE_LOOKUP[tokens[i]] < COMBINED_VALUE_LOOKUP[tokens[i+1]]:
            return False        

    return True


def _rule_2(tokens: list[str]) -> bool:
    """
    M, C, and X cannot be equalled or exceeded by smaller denominations.

    Examples:
        >>> _rule_2(['X'] + (['I'] * 9))
        True
        >>> _rule_2(['X'] + (['I'] * 10))
        False

    Args:
        tokens (list[str]):
            The list of tokens returned by the `tokenize` method.
        
    Returns:
        bool
    """
    count = Counter(tokens)

    for numeral in ["M", "C", "X"]:
        index = NUMERAL_ORDER.index(numeral)
        lower_denoms = NUMERAL_ORDER[index+1:]

        for lower in lower_denoms:
            value = NUMERAL_VALUE_LOOKUP[lower] * count[lower]

            if value >= NUMERAL_VALUE_LOOKUP[numeral]:
                return False

    return True


def _rule_3(tokens: list[str]) -> bool:
    """
    D, L, and V can each only appear once.

    Examples:
        >>> _rule_3(['X', 'V', 'I', 'V'])
        False

    Args:
        tokens (list[str]):
            The list of tokens returned by the `tokenize` method.
        
    Returns:
        bool    
    """
    count = Counter(tokens)

    if (count['D'] > 1) or (count['L'] > 1) or (count['V'] > 1):
        return False
    
    return True


def _rule_4(tokens: list[str]) -> bool:
    """
    Subtractive pairs can only be used once.

    Examples:
        >>> _rule_4(['IX', 'IV'])
        True
        >>> _rule_4(['IX', 'IX'])
        False

    Args:
        tokens (list[str]):
            The list of tokens returned by the `tokenize` method.
        
    Returns:
        bool    
    """
    count = Counter(tokens)

    for _ in count:
        if (len(_) == 2) and (count[_] != 1):
            return False    

    return True

#endregion
 

#region Validation

def validate_numeral(s: str) -> None:
    # Clean the strings
    if s == "":
        raise ValueError(f"Numeral string is empty: '{s}'")

    if not contains_only_numerals(s):
        raise ValueError(f"Contains characters other than numerals: '{s}'")

    if is_mixed_case(s):
        raise ValueError(f"Numerals must be of the same case: '{s}'")

    # Now string is clean, we can split it tokens and check for the 4 rules.
    tokens = tokenize(s)

    # Project Euler defined these rules, i have changed the order so they are 
    # applied in a fail-first style.
    if not _rule_3(tokens):
        raise ValueError(f"D, L, and V can each only appear once. '{s}'")

    if not _rule_4(tokens):
        raise ValueError(f"Subtractive pairs can only be used once. '{s}'")

    if not _rule_1(tokens):
        raise ValueError(f"Numerals must be arranged in descending order of size. '{s}'")
    
    if not _rule_2(tokens):
        raise ValueError(f"M, C, and X cannot be equalled or exceeded by smaller denominations.. '{s}'")   


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

#endregion