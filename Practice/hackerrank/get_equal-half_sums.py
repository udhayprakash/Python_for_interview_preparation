#!/usr/bin/python3
"""
Purpose: In the given list of numbers,
    return two lists of equal sums
"""


def myfunc(arr):
    half = sum(arr) / 2
    part_sum = 0
    for index, num in enumerate(arr):
        part_sum += num
        if part_sum >= half:
            break
    else:
        return -1
    return [arr[: index + 1], arr[index + 1 :]]


print(myfunc([1, 1, 1, 2, 1]))
assert myfunc([1, 1, 1, 2, 1]) == [[1, 1, 1], [2, 1]]
assert myfunc([2, 2]) == [[2], [2]]
assert myfunc([1, 2, 3, 4, 6, 4]) == [[1, 2, 3, 4], [6, 4]]
