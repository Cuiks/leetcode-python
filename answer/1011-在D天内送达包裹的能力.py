from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            days = 1
            day_weight = 0
            for weight in weights:
                if day_weight + weight > mid:
                    days += 1
                    day_weight = 0
                day_weight += weight
            if days <= D:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D = 5
    print(Solution().shipWithinDays(demo, D))
