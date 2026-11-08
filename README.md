# Roman Numerals

A Python project to represent and work with Roman Numerals. Just a fun mini-project, because why not?

Originally wrote the code as part of my solution to https://projecteuler.net/problem=89

See `main.py` for a usage example.

DEVA SEMPER!

# links
- https://projecteuler.net/about=roman_numerals
- https://en.wikipedia.org/wiki/Roman_numerals

# Notes

```python
NUMERALS = { 'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
```

`LCD` numerals can sometimes be hard to remember, so a good mnemonic is `Liquid Crystal Display`.

# Numeral

- Only numbers between 1 and 9,999 inclusive are supported
- Stores a numeral as a numeral, value & minimal numeral

# PlaceValues

Contains a `PlaceValues` class that splits numbers into thousands, hundreds, tens & units. Also decomposes them into their component parts.

Example:
```python
>>> PlaceValues(1600).decompose()
[1000, 600, 0, 0]

>>> PlaceValues(1600).decompose(as_strings=True)
['1000', '600', '00', '0']
```

# Validation

## Overview

A numeral is considered valid if it contains only valid numerals, has no spaces, uses the same letter case throughout, and follows the four basic validation rules.

1. Numerals must be arranged in descending order of size.
2. M, C, and X cannot be equalled or exceeded by smaller denominations.
3. D, L, and V can each only appear once. 
4. Subtractive pairs can only be used once. 

## Subtractive Pair Rule

Only I, X, and C are used subtractively in the standard system:
- I can precede V or X.
- X can precede L or C.
- C can precede D or M.

|     | Thousands | Hundreds |  Tens  | Units  |
| :-: | :-------: | :------: | :----: | :----: |
|  1  |     M     |    C     |   X    |   I    |
|  2  |    MM     |    CC    |   XX   |   II   |
|  3  |    MMM    |   CCC    |  XXX   |  III   |
|  4  |     -     |  **CD**  | **XL** | **IV** |
|  5  |     -     |    D     |   L    |   V    |
|  6  |     -     |    DC    |   LX   |   VI   |
|  7  |     -     |   DCC    |  LXX   |  VII   |
|  8  |     -     |   DCCC   |  LXXX  |  VIII  |
|  9  |     -     |  **CM**  | **XC** | **IX** |
