#!/usr/bin/python
"""
Purpose: WAP to check whether a given integer is
palindrome or not, without using Python builtins
"""


def is_number_palindrome(number):
    temp = number
    rev = 0
    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10
    return True if temp == rev else False


if __name__ == "__main__":
    assert is_number_palindrome(123) is False
    assert is_number_palindrome(121) is True
