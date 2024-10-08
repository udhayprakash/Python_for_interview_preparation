#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Given a sorted array nums, remove the duplicates in-place such that each
     element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    assert Solution().removeDuplicates([1, 1, 2]) == 2
    assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
