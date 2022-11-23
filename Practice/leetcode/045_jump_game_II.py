from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums[0] == 0:
            return 0
        arrlen = len(nums)
        if arrlen <= 1:
            return 0
        if arrlen == 2:
            return 1
        index = 0
        jumps_count = 0
        while index < arrlen:
            jumps_count += 1
            print("jum", jumps_count)
            sub_arr = nums[index + 1 : index + nums[index] + 1]
            print("sub_arr", sub_arr)

            if not sub_arr:
                break
            if len(sub_arr) == 1:
                if index + nums[index] + 1 < arrlen:
                    jumps_count += 1
                break
            index += max(sub_arr)
        return jumps_count


assert Solution().jump([1, 3, 2]) == 2
# print(Solution().jump([1, 2, 3]))

# print(Solution().jump([2, 3, 1]))
# print(Solution().jump([2, 3, 1, 1, 5]))
# print(Solution().jump([4]))
# print(Solution().jump([5,2,1,1,4,8,2,1,0,0,0,1,2,10,2,1]))
# print(Solution().jump([2,2,2,2,2]))
# print(Solution().jump([2,2,2,2,2,2]))
# print(Solution().jump([0,2,1,1,4,8,2,1,0,0,0,1,2,10,2,1]))
