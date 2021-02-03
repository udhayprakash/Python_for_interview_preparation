#!/usr/bin/python
"""
Purpose: Reverse a number
    1. Using  iteration
    2. Using Recursion

"""

# Method 1 - Using Iteration


def reverse_integer(number):
    result = 0
    while number > 0:
        remainder = number % 10
        result = (result * 10) + remainder
        number //= 10
    return result


assert reverse_integer(123) == 321
assert reverse_integer(100) == 1
assert reverse_integer(101) == 101


# Method 2 - Using Recursion
_result = 0


def reverse_integer(number):
    global _result
    if number <= 0:
        return _result
    else:
        remainder = number % 10
        _result = (_result * 10) + remainder
        return reverse_integer(number//10)


assert reverse_integer(123) == 321
_result = 0
assert reverse_integer(100) == 1
_result = 0
assert reverse_integer(101) == 101
