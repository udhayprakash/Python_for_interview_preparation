#!/usr/bin/python
"""
Purpose:
Example 1: Calculating sum of a list of numbers
"""
# Method 1 : conventional implementation
def sum_of_list(num_list):
    summation = 0
    for num in num_list:
        summation += num
    return summation


print(sum_of_list([12, 23, 34, 546, 1]))


# Method 2 : implementation using recursions
def sum_of_list_rec(num_list):
    if len(num_list) == 1:
        return num_list[0]
    print(f"{num_list =}")
    return num_list[0] + sum_of_list_rec(num_list[1:])


print(sum_of_list_rec([12, 23, 34, 546, 1]))

# 12 +  [23, 34, 546, 1]
# 12 +  23 +  [34, 546, 1]
# 12 +  23 +   34 + [546, 1]
# 12 +  23 +   34 + 546  +[1]
# 12 +  23 +   34 + 546  + 1
# 12 +  23 +   34 + 546  + 1 + 0


def sum_of_list_rec2(num_list):
    if not num_list:  # num_list == []:
        return 0
    print(f"{num_list =}")
    return num_list[0] + sum_of_list_rec2(num_list[1:])


print(sum_of_list_rec2([12, 23, 34, 546, 1]))
