# Компьютерная игра
n = int(input())
t = [0] + list(map(int, input().split()))
# print(t)
dp = [0, 0, abs(t[2] - t[1])]
for i in range(3, n + 1):
    dp.append(min(dp[i - 1] + abs(t[i] - t[i - 1]), dp[i - 2] + 3 * abs(t[i] - t[i - 2])))
# print(dp)
print(dp[n])
