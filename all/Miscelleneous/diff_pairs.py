#!/usr/bin/python
"""
Purpose:
    Given an Array A of N integers, return True
    if A contains atleast two elements which 
    differ by 1 , and False otherwise.
"""


def solution(A):
    A.sort()
    for index, element in enumerate(A):
        if index and (element - A[index - 1]) == 1:
            return True
    return False


if __name__ == '__main__':
    assert solution([7]) is False
    assert solution([4, 3]) is True
    assert solution([11, 1, 8, 12, 14]) is True
    assert solution([4, 10, 8, 5, 9]) is True
    assert solution([5, 5, 5, 5, 5]) is False
    assert solution([-5, -5, -5, -5]) is False
    assert solution([-5, -5, -5, 6]) is False
    assert solution([-5, -5, -5, -6]) is True
    assert solution([-3, -1, 0]) is True
