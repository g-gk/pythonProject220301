# Город Че
n, r = map(int, input().split())
d = list(map(int, input().split()))
i, j, ans = 0, 1, 0
while i < n - 1 and j < n:
    if d[j] - d[i] <= r:
        j += 1
    else:
        ans += n - j
        i += 1
print(ans)
