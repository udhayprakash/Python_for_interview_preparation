#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive), prove that at least one duplicate number
must exist. Assume that there is only one duplicate number, find the
duplicate one.

Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

"""
from typing import List


class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     for num in nums:
    #         if nums.count(num) > 1:
    #             return num

    def findDuplicate(self, nums: List[int]) -> int:
        found = []
        for num in nums:
            if num in found:
                return num
            found.append(num)


if __name__ == "__main__":
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3
