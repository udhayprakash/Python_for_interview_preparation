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
    given_list = sorted({i for i in given_list if i > 0})
    if not given_list:
        return 1
    for _index, current_pos_num in enumerate(given_list):
        if _index == 0 and current_pos_num != 1:
            return 1
        if _index:
            previous_pos_num = given_list[_index - 1]
            if current_pos_num - previous_pos_num > 1:
                return previous_pos_num + 1
    return current_pos_num + 1


def get_first_missing_pstv_num(given_list):
    given_list = sorted({i for i in given_list if i > 0})
    if (not given_list) or given_list[0] != 1:
        return 1
    for _index, num in enumerate(given_list):
        if _index and num - given_list[_index - 1] > 1:
            return given_list[_index - 1] + 1
    return given_list[-1] + 1


if __name__ == "__main__":
    assert get_first_missing_pstv_num([3, 4, -1, 1]) == 2
    assert get_first_missing_pstv_num([1, 2, 0]) == 3
    assert get_first_missing_pstv_num([2, 3, 7, 6, 8, -1, -10, 15]) == 1
    assert get_first_missing_pstv_num([1, 3, 6, 4, 1, 2]) == 5
    assert get_first_missing_pstv_num([1, 2, 3]) == 4
    assert get_first_missing_pstv_num([-1, -3]) == 1
