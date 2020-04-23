#!/usr/bin/python
"""
Purpose:  https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
"""


def linear_search(given_array, search_ele):
    for _index, ele in enumerate(given_array):
        if ele == search_ele:
            return _index

    return -1


if __name__ == '__main__':
    assert linear_search([1, 2, 3, 4, 5, 6, 7], 6) == 5
    assert linear_search([3, 4, 2, 6, 5, 1, 7], 6) == 3
    assert linear_search([3, 4, 2, 6, 5, 1, 7], -6) == -1
    assert linear_search([3, 4, 2, 6, [6], 1, 7], [6]) == 4
