"""
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it is able to trap after raining.
"""

case_1 = [1, 2, 3]  # 0
case_2 = [1, 0, 1]  # 1
case_3 = [3, 2, 1, 4, 0, 4]  # 4

# 3, 2, 1, 4
# 4, 1, 3


def find_largest_puddle(arr):
    max_size = 0
    p_start = arr[0]
    for height in arr:
        if height >= p_start:
            size = min(height, p_start)
            if size > max_size:
                max_size = size

    return max_size


print(find_largest_puddle([1, 2, 3]))
