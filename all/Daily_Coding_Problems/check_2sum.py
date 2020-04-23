#!/usr/bin/python
"""
Purpose:
Given a list of numbers and a number k, return whether any two numbers from the list
add up to k.

Example:
        input   :  [10, 15, 3, 7] & k=17
        output  :  True ( as 10 + 7 = 17)
"""


def check_2_sum(given_list, k):
    """
    This function will check whether the given value, k, is
    a summation of any two numbers in the given list.
    :param given_list: Given list of values
    :param k: summation value to check
    :return: True or False
    """
    for _index1, ele1 in enumerate(given_list):
        for ele2 in given_list[_index1:]:
            if ele1 + ele2 == k:
                print(f'{ele1} + {ele2} == {k}')
                return True
    return False


if __name__ == '__main__':
    assert check_2_sum([10, 15, 3, 7], k=17) is True
    assert check_2_sum([-1, -3, 4, 5], k=4) is True
    assert check_2_sum([2.5, 4.6, 2.1, 7], k=4.6) is True
