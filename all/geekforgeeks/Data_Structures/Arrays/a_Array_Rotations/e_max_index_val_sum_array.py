#!/usr/bin/python
"""
Purpose:  https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/
Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed

"""


def array_rotation(given_array, shift_positions):
    """ 
    Pythonic way 
        Time complexity : O(n)
        Auxiliary Space : O(shift_positions)
    """
    return given_array[shift_positions:] + given_array[:shift_positions]


def get_max_count(arr):
    max_count = 0
    for _index, _ in enumerate(arr):
        shifted_array = array_rotation(arr, _index)
        count = 0
        for _index2, val2 in enumerate(shifted_array):
            count += _index2 * val2
        if count > max_count:
            max_count = count
    return max_count


def get_max_count(arr):
    """
        Time Complexity : O(n)
        Auxiliary Space : O(1)
    """
    # stores sum of arr[i] 
    arrSum = 0

    # stores sum of i*arr[i] 
    currVal = 0

    n = len(arr)

    for i in range(0, n):
        arrSum += arr[i]
        currVal += (i * arr[i])

        # initialize result
    maxVal = currVal

    # try all rotations one by one and find the maximum  
    # rotation sum 
    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n - j]
        if currVal > maxVal:
            maxVal = currVal

    return maxVal


if __name__ == '__main__':
    assert get_max_count([1, 20, 2, 10]) == 72
    assert get_max_count([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 330
