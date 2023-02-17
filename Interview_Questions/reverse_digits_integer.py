"""
Problem: Given an integer, return the integer with reversed digits.

    NOTE: The integer could be either positive or negative.
    Example:
        input: -231, the expected output is -132
        input: 345, the expected output is 543
"""


def reverse_digits(number):
    sign = -1 if number < 0 else 1
    number = abs(number)

    rev_number = 0
    while number:
        divisor, remainder = divmod(number, 10)
        rev_number = 10 * rev_number + remainder
        number = divisor
    return rev_number * sign


assert reverse_digits(-231) == -132
assert reverse_digits(345) == 543
