#!/usr/bin/python
"""
Purpose: Factorial
    Ex: factorial(5) = 5 * 4 * 3 * 2 * 1
        factorital(50) = 50 * 49 * 48 * ....... * 2 * 1
"""
# Method 1 - pythonic way
from functools import reduce

result = reduce(lambda x, y: x * y, range(1, 5 + 1))  # (((1* 2)* 3) * 4) * 5
print(result)

# Method 2 - using math module
import math

print(f"{math.factorial(5) =}")
print(f"{math.factorial(22) =}")


# Method 3 - using iterations
def factorial_iteration(num):
    result = 1
    for each_num in range(1, num + 1):
        result *= each_num
    return result


print(f"{factorial_iteration(5)  =}")
print(f"{factorial_iteration(22) =}")
# print(f'{factorial_iteration(12345) =}')

# Method 4 - using recursions
def factorial_rec(num):
    print(f"{recursion_number =}")
    if num <= 1:
        return 1
    # print(f'{num =}')
    return num * factorial_rec(num - 1)


# factorial_rec(5)
# 5 * factorial_rec(4)
# 5 * 4 * factorial_rec(3)
# 5 * 4 * 3 * factorial_rec(2)
# 5 * 4 * 3 * 2 * factorial_rec(1)
# 5 * 4 * 3 * 2 * 1
print()
print(f"{factorial_rec(5)   =}")
print(f"{factorial_rec(22)  =}")
# print(f'{factorial_rec(12345) =}')
