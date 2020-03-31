#!/usr/bin/python
"""
Purpose:
    recursive_power is a function that computes x to the power n.
    n can be positive, 0 or negative.
    E g. recursive_power(2,3) returns 8, (Because 2^3 is 2*2*2 three times which is 8)
    E.g. recursive_power(3, -2) returns 1/9 (Because 3^-2 is 1/(3^2)), …. and so on.
    Do this using ‘recursion’. (If you don’t know about recursion, do it iteratively)
    Don’t use a library function like Math.pow() or direct expressions like x^y, or x**y. Use basic multiplication.

"""


def recursive_power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return (1 / x) * recursive_power(x, n + 1)
    else:
        return x * recursive_power(x, n - 1)


assert recursive_power(2, 3) == 8
assert recursive_power(2, 0) == 1
assert recursive_power(2, -3) == 0.125
