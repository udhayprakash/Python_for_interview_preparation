#!/usr/bin/python3
"""
Problem:
Given an array of integers nums sorted in ascending order, find the starting
and ending positions of a given target values.

If target is not found in the array, return [-1, -1]

"""


def find_first_n_last_indices(arr, target_value):
    positions = []
    for index, value in enumerate(arr):
        if value == target_value:
            positions.append(index)
    if not positions:
        return [-1, -1]
    return [positions[0], positions[-1]]


def find_first_n_last_indices(arr, target_value):
    startIndex, finalIndex = -1, -1
    for index, value in enumerate(arr):
        if value == target_value:
            if startIndex == -1:
                startIndex = index
            else:
                finalIndex = index
    if startIndex == -1:
        return [-1, -1]
    if finalIndex == -1:
        return [startIndex, startIndex]
    return [startIndex, finalIndex]


assert find_first_n_last_indices([5, 7, 7, 8, 8, 8, 10], 8) == [3, 5]
#                                 0  1  2  3  4   5
assert find_first_n_last_indices([5, 7, 7, 8, 8, 8, 10], 5) == [0, 0]
assert find_first_n_last_indices([5, 7, 7, 8, 8, 8, 10], 3) == [-1, -1]
