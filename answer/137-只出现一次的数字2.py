from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        if length == 1:
            return nums[0]
        for i in range(0, length):
            if i == 0 and nums[i] != nums[i + 1]:
                return nums[i]
            if i == length - 1 and nums[i] != nums[i - 1]:
                return nums[i]
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]


print(Solution().singleNumber([2, 2, 3, 2]))
