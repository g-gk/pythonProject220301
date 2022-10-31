# Сумма подряд идущих
# n, k, m = 4, 1, -1
# a = [9, 13, 10, -11]
n, m = map(int, input().split())
h = list(map(int, input().split()))
p = [0] * (n + 1)
for i in range(1, n):
    p[i + 1] = p[i]
    if h[i] > h[i - 1]:
        p[i + 1] += 1
# print(p)
ans = []
for i in range(m):
    l, r = map(int, input().split())
    ans += [p[r] - p[l]]
print('\n'.join(map(str, ans)))
