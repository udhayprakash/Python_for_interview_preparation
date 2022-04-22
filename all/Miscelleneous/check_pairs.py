#!/usr/bin/python
"""
Purpose: Given an array of integers, create
paits of them, such that every pair consists
of equal numbers. Each array elements may belong
to one pair only. Is it possible to use all integers?

"""


def solution(A):
    for each_ele in A:
        if A.count(each_ele) % 2:
            return False
    return True


if __name__ == "__main__":
    assert solution([1, 2, 2, 1]) is True
    assert solution([7, 7, 7]) is False
    assert solution([1, 2, 2, 3]) is False
    assert solution([1]) is False
    assert solution([2]) is False
