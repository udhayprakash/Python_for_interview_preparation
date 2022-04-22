#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/single-number/

    Given a non-empty array of integers, every element appears
    twice except for one. Find that single one.

NOTE: Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?


"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:  # O(n)
        for num in nums:
            if nums.count(num) == 1:
                return num

    def singleNumber(self, nums: List[int]) -> int:  # O(1)
        """
        Utilize the property of XOR, A ⊕ A = 0, to cancel
        those elements which appeared twice.
            (1) XOR(zero, number)-> number
            (2) XOR(number, number)-> zero
        """
        xor_result = 0
        for x in nums:
            xor_result ^= x

        return xor_result


if __name__ == "__main__":
    assert Solution().singleNumber([2, 2, 1]) == 1
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
