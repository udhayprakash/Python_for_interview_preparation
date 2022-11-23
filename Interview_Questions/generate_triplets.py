#!/usr/bin/python3
"""
Purpose:
    Given an array A = [1, 4, 7, 3, 9, 0, 10, 13, 11, 2, 5, 14]
    (of unique elements )
    Find all triplets that add up to X
    Eg:- If x = 12
    Solution set would be
    [[1, 4, 7], [1, 2, 9], [1, 0, 11], [4, 3, 5], [7, 3, 2] . . . ]
"""


from collections import defaultdict
from pprint import pprint


def generate_triplets(given_array, expected_sum):  # O(n^3)
    triplets = []
    for val1 in given_array:
        for val2 in given_array:
            for val3 in given_array:
                if val1 + val2 + val3 == expected_sum:
                    triplets.append([val1, val2, val3])
                    print([val1, val2, val3])
    return triplets


def generate_triplets(given_array, expected_sum):
    triplets = []
    temp = defaultdict(list)  # 11: [[1], []]
    for val in given_array:
        remaining = expected_sum - val
        if remaining >= 0:
            temp[remaining].append([val])
    pprint(temp)


"""
{
    1: [],
    4: [],
    7: [],
    3: [],
    9: [],
    0: [],
    10:[],
    11:[],
    2: [],
    5: [],

#  13: [],
   # 14: []
}

"""
if __name__ == "__main__":
    A = [1, 4, 7, 3, 9, 0, 10, 13, 11, 2, 5, 14]
    generate_triplets(A, 12)
