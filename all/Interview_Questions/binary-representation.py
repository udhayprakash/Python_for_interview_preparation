#!/usr/bin/python3
"""
Question
--------
Given an integer "n", return an array "a" of length
"n+1" such that for each "i" (0<=i<=n), a[i] is the
number of 1's in the binary representation of "i".

"""
# memoization design pattern, to store already computed results, for reuse
binaryNumMap = {}


def integerToBinary(number):
    """This function will convert integers, to binary form string"""
    result = ""
    if number >= 1:
        result += str(integerToBinary(number // 2))
    result += str(number % 2)
    return result


def binaryRepresentation(n):
    if n < 0:
        return "invalid input"
    result = []
    for i in range(n + 1):  # n+1, as range will not include last value in boundary

        if not (i in binaryNumMap):
            binaryNumMap[i] = integerToBinary(i).count("1")

        result.append(binaryNumMap[i])
    return result


assert binaryRepresentation(-1) == "invalid input"
assert binaryRepresentation(0) == [0]
assert binaryRepresentation(5) == [0, 1, 1, 2, 1, 2]
assert binaryRepresentation(11) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3]
assert binaryRepresentation(27) == [
    0,
    1,
    1,
    2,
    1,
    2,
    2,
    3,
    1,
    2,
    2,
    3,
    2,
    3,
    3,
    4,
    1,
    2,
    2,
    3,
    2,
    3,
    3,
    4,
    2,
    3,
    3,
    4,
]
