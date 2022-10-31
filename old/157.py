# Покупка билетов
n = int(input())
t = [(0, 0, 0)]
t += [tuple(map(int, input().split())) for _ in range(n)]
# print(t)
dp = [0] * (n + 1)
if n == 1:
    print(t[1][0])
elif n == 2:
    print(min(t[1][0] + t[2][0], t[1][1]))
else:
    dp[1] = t[1][0]
    dp[2] = min(t[1][0] + t[2][0], t[1][1])
    for i in range(3, n + 1):
        dp[i] = min(t[i][0] + dp[i - 1],
                    t[i][0] + t[i - 2][1] + dp[i - 3],
                    t[i - 2][0] + t[i - 1][1] + dp[i - 3],
                    t[i - 2][2] + dp[i - 3],
                    t[i - 1][1] + dp[i - 2])
    # print(dp)
    print(dp[n])
