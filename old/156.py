# Гвоздики
n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 2:
    print(a[1] - a[0])
elif n == 3:
    print(a[2] - a[0])
else:
    dp = [0, a[1] - a[0], a[2] - a[0]]
    for i in range(3, n):
        dp.append(min(a[i] - a[i - 1] + dp[i - 1], a[i] - a[i - 1] + dp[i - 2]))
    print(dp[n - 1])
