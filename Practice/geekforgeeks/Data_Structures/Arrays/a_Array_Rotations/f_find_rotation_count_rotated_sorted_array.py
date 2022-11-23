#!/usr/bin/python
"""
Purpose:  https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

    Consider an array of distinct numbers sorted in increasing order.
    The array has been rotated (clockwise) k number of times.
    Given such an array, find the value of k.
"""


def array_rotation(given_array, shift_positions):
    """
    Pythonic way
        Time complexity : O(n)
        Auxiliary Space : O(shift_positions)
    """
    return given_array[shift_positions:] + given_array[:shift_positions]


def is_sorted(arr):
    min_val = arr[0]
    for val in arr[1:]:
        if val < min_val:
            return False
    return True


def find_rotation_count(given_arr):
    for _index, _ in enumerate(given_arr):
        shifted_array = array_rotation(given_arr, _index)
        if is_sorted(shifted_array):
            return _index
        # print(shifted_array, is_sorted(shifted_array))


if __name__ == "__main__":
    assert find_rotation_count([15, 18, 2, 3, 6, 12]) == 2
    assert find_rotation_count([7, 9, 11, 12, 5]) == 4
    assert find_rotation_count([7, 9, 11, 12, 15]) == 0
