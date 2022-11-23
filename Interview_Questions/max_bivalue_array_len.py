"""
Find the maximum bivalued sub-array length, from the given array
"""


def solution(A):
    if not A:
        return 0
    max_bival_arr_len = 0
    for i, _ in enumerate(A):
        for each in (A[i:], A[:-i], A[i + 1 : -i - 1]):
            val = is_max(each, max_bival_arr_len)
            if val != 0:
                max_bival_arr_len = val
    return max_bival_arr_len


def is_max(arr, max_val):
    if is_bivalued(arr) and len(arr) > max_val:
        return len(arr)
    return 0


def is_bivalued(arr):
    return len(set(arr)) <= 2


assert solution([0, 5, 4, 4, 5, 12]) == 4
assert solution([5, 4, 4, 5]) == 4

print(solution([5, 4, 4, 5]))
