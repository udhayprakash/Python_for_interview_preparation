#!/usr/bin/python
"""
Purpose:  This problem is asked in `Stripe`
    Given an array of integers, find the first missing positive integer
    in linear time and constant space. In other words, find the lowest
    positive integer that does not exit in the array.

Example:
    input : [3, 4, -1, 1]
    output: 2

    input : [1, 2, 0]
    output: 3
"""


def get_first_missing_pstv_num(given_list):
    given_list.sort()
    for _index, num in enumerate(given_list):
        if _index and num > 0 and given_list[_index - 1] > 0:
            print(num, given_list[_index - 1], num - given_list[_index - 1])


if __name__ == '__main__':
    get_first_missing_pstv_num([3, 4, -1, 1])
    assert get_first_missing_pstv_num([3, 4, -1, 1]) == 2
    assert get_first_missing_pstv_num([1, 2, 0]) == 3
