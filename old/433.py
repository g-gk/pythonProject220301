# Торговля акциями
n, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d1, d2, aim = 0, 0, 0
for j in range(1, n):
    if a[j - 1] < a[aim]:
        aim = j - 1
    # if b[j] > a[aim] and (d2 == 0 or b[j] - a[aim] > b[d2] - a[d1]):
    if (b[j] > a[aim] and
            (d2 == 0 or
             x // a[aim] * b[j] + x % a[aim] > x // a[d1] * b[d2] + x % a[d1])):
        d1, d2 = aim, j
ans = x // a[d1] * b[d2] + x % a[d1]
if d2 != 0 and ans > x:
    print(ans)
    print(d1 + 1, d2 + 1)
else:
    print(x)
    print(-1, -1)
