
from typing import Counter

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
    "CM": 900, "cm": 900,
}

COMBINED_LOOKUP = NUMERAL_LOOKUP | SUBTRACTIVE_PAIRS_LOOKUP


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
    only valid numerals, 
    # ['IX', ' ', 'IX', ' ', 'G', ' ', 'V']
    # ['IX', 'IX', 'V']

    Splits a string of numerals into UPPERCASE tokens which are either a numeral, or a pair of subtractive numerals.

    DOESN'T check for validity. For Example, "IXIX" becomes ["IX", "IX"]

    Examples:
        >>> tokenize("IXX")
        ['IX', 'X']

        >>> tokenize("XIX")
        ['X', 'IX']

        >>> tokenize("XXI")
        ['X', 'X', 'I']

        >>> tokenize("XIXIX")
        ['X', 'IX', 'IX']

    Args:
        numeral_str (str):
            A string containing ONLY roman numerals.

    Returns:
        list[str]:
            A list of uppercase tokens.
    """
    line = numeral_str.upper() # So we don't have 'iX' for example
    tokens = []
    
    while len(line) > 0:
        if line[0:2] in SUBTRACTIVE_PAIRS_LOOKUP:
            tokens.append(line[0:2])
            line = line[2:]

        elif line[0] in NUMERAL_LOOKUP:
            tokens.append(line[0])
            line = line[1:]

        else:
            tokens.append(line[0])
            line = line[1:]

    return [t for t in tokens if t in NUMERAL_LOOKUP | SUBTRACTIVE_PAIRS_LOOKUP]




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
    if len(tokens) == 0:
        return False

    if len(tokens) == 1:
        return True

    for i in range(len(tokens)-1):
        if COMBINED_LOOKUP[tokens[i]] < COMBINED_LOOKUP[tokens[i+1]]:
            return False        

    return True


def _rule_2(tokens: list[str]) -> bool:
    pass


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
    c = Counter(tokens)

    if (c['D'] > 1) or (c['L'] > 1) or (c['V'] > 1):
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
    c = Counter(tokens)

    for _ in c:
        if (len(_) == 2) and (c[_] != 1):
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

    if not _rule_1(tokens):
        raise ValueError(f"Numerals must be arranged in descending order of size. '{s}'")

    if not _rule_3(tokens):
        raise ValueError(f"D, L, and V can each only appear once. '{s}'")

    if not _rule_4(tokens):
        raise ValueError(f"Subtractive pairs can only be used once. '{s}'")


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