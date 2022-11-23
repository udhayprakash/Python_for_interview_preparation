#!/usr/bin/python
"""
Purpose:    This problem was asked in Uber interview.
Given an array of integers, return a new array such that
each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

"""


def product_all_except_it(given_list):
    result = []
    for _index, _ in enumerate(given_list):
        temp_list = given_list[:_index] + given_list[_index + 1 :]
        product = 1
        for each_ele in temp_list:
            product *= each_ele
        result.append(product)
    return result


if __name__ == "__main__":
    product_all_except_it([1, 2, 3, 4, 5])
    assert product_all_except_it([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24], "first"
    assert product_all_except_it([3, 2, 1]) == [2, 3, 6]
    assert product_all_except_it([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert product_all_except_it([1, 0, 1, 1]) == [0, 1, 0, 0]
    assert product_all_except_it([-1, 0, -1, 1]) == [0, 1, 0, 0]
    assert product_all_except_it([-1, 0, 1, 1]) == [0, -1, 0, 0]
