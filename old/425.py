# Торговля акциями
# n, x = 5, 1000
# a = list(map(int, '3 9 8 1 6'.split()))
# b = list(map(int, '9 11 7 14 13'.split()))
n, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ib, jb, aim, bim = 0, 0, 0, 0
for j in range(1, n):
    if a[j - 1] < a[aim]:
        aim = j - 1
    if b[j] > a[aim] and (jb == 0 or b[j] - a[aim] > b[jb] - a[ib]):
        ib, jb = aim, j
ans = x + x // a[ib] * (b[jb] - a[ib])
if jb != 0 and ans > x:
    print(ans)
    print(ib + 1, jb + 1)
else:
    print(x)
    print(-1, -1)
