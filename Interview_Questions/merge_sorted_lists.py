#!/usr/bin/python3
"""
Problem: Merge two sorted lists
"""


def mergeSortedLists(a1, a2):
    a3 = []
    a1_len = len(a1)
    a2_len = len(a2)
    a1_index = 0
    a2_index = 0
    for _ in range(a1_len + a2_len):
        if a1_index >= a1_len:
            a3.extend(a2[a2_index:])
            return a3
        elif a2_index >= a2_len:
            a3.extend(a1[a1_index:])
            return a3
        a1_item = a1[a1_index]
        a2_item = a2[a2_index]
        if a1_item < a2_item:
            a3.append(a1_item)
            a1_index += 1
        elif a2_item < a1_item:
            a3.append(a2_item)
            a2_index += 1
        else:
            a3.extend([a1_item] * 2)  # to store dups
            a1_index += 1
            a2_index += 1
    return a3


# [0, 1, 1, 3, 4, 7, 7, 20]
print(mergeSortedLists([1, 4, 7, 20], [0, 1, 3, 7]))


def mergeSortedLists(a1, a2):
    return sorted(a1 + a2)


# [0, 1, 1, 3, 4, 7, 7, 20]
print(mergeSortedLists([1, 4, 7, 20], [0, 1, 3, 7]))
