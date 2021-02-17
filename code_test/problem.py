#!/usr/bin/python3
"""
Purpose:
Please write pyest that covers all scenarios and we will review code in the interview.
Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k positions clock-wise, 
we define a "rotation function" F on A as follow:
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
Calculate the maximum and minimum value of F(0), F(1), ..., F(n-1).
Note:
n is guaranteed to be less than 105.
Make sure list of elements are non-negative
Sample input and output is : Basically, you are shifting number from right to left for 
each f(x).
4, 3, 2, 6
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
Minimum value of F(0), F(1), F(2), F(3) is F(3) = 16
"""


class Solution(object):
    def max_n_min_rotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        array_sum = sum(A)
        array_count = 0
        for _index, value in enumerate(A):
            array_count += _index * value

        result_max = result_min = array_count
        for i in range(len(A) - 1, 0, -1):
            array_count += array_sum - (len(A) * A[i])
            result_max = max(array_count, result_max)
            result_min = min(array_count, result_min)
        return result_max, result_min

    def max_n_min_rotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_val = min_val = 0
        for _index, _ in enumerate(A):
            shift_array = A[_index:] + A[:_index]
            array_sum = sum(
                [indx * val for indx, val in enumerate(shift_array)])
            if _index:
                if array_sum < min_val:
                    min_val = array_sum
                if array_sum > max_val:
                    max_val = array_sum
            else:
                min_val = max_val = array_sum

        return max_val, min_val


if __name__ == '__main__':
    print(Solution().max_n_min_rotation([]))
    assert Solution().max_n_min_rotation([]) == (0, 0)
    assert Solution().max_n_min_rotation([4, 3, 2, 6]) == (26, 16)
