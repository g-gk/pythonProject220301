# Энты
k, p = map(int, input().split())
dp = [0, 0, 1]
for i in range(3, k + 1):
    dp.append(dp[-1])
    if i % 2 == 0:
        dp[i] += dp[i // 2]
    dp[i] %= p
# print(dp)
print(dp[k] % p)
