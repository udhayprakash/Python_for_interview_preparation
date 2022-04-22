#!/usr/bin/python3
"""
Problem:

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [-1, -3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    A = sorted({num for num in A if num > 0})
    if not A:
        return 1
    for index, num in enumerate(A):
        if index == 0:
            continue
        if num - A[index - 1] > 1:
            return A[index - 1] + 1

    return A[-1] + 1


if __name__ == "__main__":
    assert solution([1, 3, 6, 4, 1, 2]) == 5
    assert solution([1, 2, 3]) == 4
    assert solution([-1, -3]) == 1
