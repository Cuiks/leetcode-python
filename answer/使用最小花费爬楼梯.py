# -*- coding: utf-8 -*-


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

n = len(cost)

dp = {}

dp[0] = dp[1] = 0

for i in range(2, n + 1):
    dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

print(dp)
print(dp[n])
