#!/usr/bin/python
"""
Purpose: Given an array, check whether all
      elements are in sorted order or not
"""


def is_sorted(given_list):
    if len(given_list) == 1:
        return True
    elif given_list[0] > given_list[1]:
        # print(given_list[0], given_list[1])
        return False
    else:
        return is_sorted(given_list[1:])


if __name__ == "__main__":
    print(f"{is_sorted([1, 2, 3, 4, 5, 6]) =}")
    print(f"{is_sorted([1, 2, 3, 5, 4, 6]) =}")
