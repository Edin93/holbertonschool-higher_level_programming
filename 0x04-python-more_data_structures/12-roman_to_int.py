#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif isinstance(roman_string, str) == False:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    l = len(roman_string)
    last = romans[roman_string[l - 1]]
    r = last
    for i in range(l - 1):
        char = roman_string[l - 2 - i]
        current = romans[char]
        if current < last:
            r -= current
        else:
            r+= current
        last = current
    return r
