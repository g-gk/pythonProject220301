# Без двух нулей подряд
n, k = map(int, input().split())
dp = [(0, 0), (1, k - 1)]
for i in range(2, n + 1):
    dp.append((dp[i - 1][1], (k - 1) * (sum(dp[i - 1]))))
print(sum(dp[n]))
