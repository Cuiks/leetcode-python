import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = 0
        self.sums = [0]
        for val in w:
            self.total += val
            self.sums.append(self.total)

    def pickIndex(self) -> int:
        if not self.w:
            return 0
        hit = random.randint(0, self.total)
        left = 0
        right = len(self.sums) - 1
        while left != right:
            mid = int((left + right) / 2)
            if hit <= self.sums[mid]:
                right = mid
            else:
                left = mid
        return left


w = [1, 3]
obj = Solution(w)
for i in range(10000):
    left, hit = obj.pickIndex()
    print(hit, left)
    # if (0 <= hit <= 3 and left != 0) or (3 < hit <= 17 and left != 1) or (17 < hit <= 18 and left != 2) or (
    #         18 < hit <= 25 and left != 3):
    #     print(hit, left)
