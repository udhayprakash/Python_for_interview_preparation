#!/usr/bin/python
"""
Purpose:  
"""


def binary_search(given_array, search_ele):
    """ Binary Search assumes that the array is already sorted
    """
    given_array.sort()
    pass


if __name__ == '__main__':
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 6) == 5
    assert binary_search([3, 4, 2, 6, 5, 1, 7], 6) == 3
    assert binary_search([3, 4, 2, 6, 5, 1, 7], -6) == -1
    assert binary_search([3, 4, 2, 6, [6], 1, 7], [6]) == 4
    assert binary_search([2, 2, 2, 2, 2, 2, 2, 2, 0, 2], 0) == 8
    assert binary_search([2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 0) == 1
