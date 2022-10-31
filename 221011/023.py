n = int(input())
a = [float(input()) for _ in range(n)]
ans = 0
for i in range(1, n - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        ans += 1
print(ans)
