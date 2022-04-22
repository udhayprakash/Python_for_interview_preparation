#!/usr/bin/python
"""
Purpose: https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
"""


def array_rev_rotation(given_array, shift_positions):
    """
    Pythonic way
        Time complexity : O(n)
        Auxiliary Space : O(shift_positions)
    """
    return given_array[-shift_positions:] + given_array[:-shift_positions]


if __name__ == "__main__":
    assert array_rev_rotation([1, 2, 3, 4, 5, 6, 7], 1) == [7, 1, 2, 3, 4, 5, 6]
    assert array_rev_rotation([1, 2, 3, 4, 5, 6, 7], 2) == [6, 7, 1, 2, 3, 4, 5]
    assert array_rev_rotation([1, 2, 3, 4, 5, 6, 7], 5) == [3, 4, 5, 6, 7, 1, 2]
    assert array_rev_rotation([1, 2, 3, 4, 5, 6, 7], 7) == [1, 2, 3, 4, 5, 6, 7]
    print(array_rev_rotation([1, 2, 3, 4, 5, 6, 7], 5))
