from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    pre = nums[0]
    i = 2
    while i < len(nums):
        if nums[i] == pre:
            i -= 1
            pre = nums.pop(i)
        else:
            pre = nums[i - 1]
        i += 1
    return len(nums)


num = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6,7,7,7,8]
# print(num.pop(2))
# print(num)
removeDuplicates(num)
print(num)
