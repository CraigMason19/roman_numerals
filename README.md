# Roman Numerals

A Python project to represent and work with Roman Numerals. Just a fun mini-project, because why not?

Originally wrote the code as part of my solution to https://projecteuler.net/problem=89

DEVA SEMPRE!

# links
- https://projecteuler.net/about=roman_numerals
- https://en.wikipedia.org/wiki/Roman_numerals

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
['1000', '600', '00', '9']
```