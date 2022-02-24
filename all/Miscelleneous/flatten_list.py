#!/usr/bin/python
"""
Purpose: List flattening
"""


def flatten(given_list, final_list=[]):
    for each_ele in given_list:
        if isinstance(each_ele, list):
            flatten(each_ele, final_list)
        else:
            final_list += [each_ele]
    return final_list


def flatten2(given_list):
    final_list = []
    for each_ele in given_list:
        if isinstance(each_ele, list):
            final_list.extend(flatten2(each_ele))
        else:
            final_list.append(each_ele)
    return final_list


if __name__ == '__main__':
    assert flatten([1, [2, 3], 4, [5, [6, [7]]]]) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten2([1, [2, 3], 4, [5, [6, [7]]]]) == [1, 2, 3, 4, 5, 6, 7]
