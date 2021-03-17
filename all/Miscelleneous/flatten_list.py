#!/usr/bin/python
"""
Purpose: List flattening
"""


def flatten_list(given_list, final_list=[]):
    for each_ele in given_list:
        if isinstance(each_ele, list):
            flatten_list(each_ele, final_list)
        else:
            final_list += [each_ele]
    return final_list


if __name__ == '__main__':
    assert flatten_list([1, [2, 3], 4, [5, [6, [7]]]]) == [1, 2, 3, 4, 5, 6, 7]
