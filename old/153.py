# Без трёх единиц
n = int(input())
if n <= 2:
    print(2 ** n)
else:
    dp = [(2, 1, 1)]
    for i in range(1, n - 1):
        x = sum(dp[i - 1])
        y = dp[i - 1][0]
        z = dp[i - 1][1]
        dp.append((x, y, z))
    # print(dp)
    print(sum(dp[n - 2]))
