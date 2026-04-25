#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    numerals_of_roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    result = 0
    prev_value = 0

    for n in reversed(roman_string):
        value = numerals_of_roman[n]

        if value >= prev_value:
            result += value
        else:
            result -= value

        prev_value = value

    return result
