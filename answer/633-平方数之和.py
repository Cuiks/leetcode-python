class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(c + 1):
            if i * i > c:
                break
            left = 0
            right = c
            mid = (left + right) // 2
            while left < right:
                res = mid * mid + i * i
                if res == c:
                    return True
                if res < c:
                    left = mid + 1
                else:
                    right = mid
                mid = (left + right) // 2
        return False


print(Solution().judgeSquareSum(0))
