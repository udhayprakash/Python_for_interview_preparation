#!/usr/bin/python
"""
Purpose: Given an integer N, returns the smallest 
integer that is greater than N and the sum of whose
digits is equal to the sum of the digits of N.
"""


def sum_of_digits_fn(num: int) -> int:
    sum_result = 0
    while num and num >= 0:
        sum_result += num % 10
        num //= 10
    return sum_result


def solution(N):
    sum_of_digits = sum_of_digits_fn(abs(N))
    while True:
        N += 1
        if sum_of_digits == sum_of_digits_fn(N):
            return N


if __name__ == '__main__':
    assert solution(28) == 37
    assert solution(734) == 743
    assert solution(1990) == 2089
    assert solution(1000) == 10000
    assert solution(-28) == 19
