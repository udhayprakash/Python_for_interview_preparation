#!/usr/bin/python
"""
Purpose: Recursion Limit
    recusion limit can be set with sys.setrecursionlimit function
    But, it cant take value more than the system RAM heap size

    Recursions will take more memory
"""
import sys

print(f"{sys.getrecursionlimit() =}")
sys.setrecursionlimit(4000)
print(f"{sys.getrecursionlimit() =}")


recursion_number = 0


def factorial_rec(num):
    global recursion_number
    recursion_number += 1
    print(f"{recursion_number =}")
    if num <= 1:
        return 1
    return num * factorial_rec(num - 1)


print()
print(f"{factorial_rec(1234) =}")
