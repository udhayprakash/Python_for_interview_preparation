"""
Problem: Perform Power Operation without using Multiplication
"""


def power(base, p):
    if base == 0:
        return 0
    if p == 0:
        return 1

    result = base
    intermediate = base
    for _ in range(1, p):
        for _ in range(1, base):
            result += intermediate
        intermediate = result
    return result


assert power(0, 12) == pow(0, 12) == 0
assert power(10, 0) == pow(10, 0) == 1
assert power(2, 4) == pow(2, 4) == 16
