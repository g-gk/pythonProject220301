# Отношение
n = int(input())
a = list(map(int, input().split()))
ib, jb, im = 0, 0, 0
for j in range(1, n):
    if a[j - 1] < a[im]:
        im = j - 1
    if a[j] / a[im] > max(1, a[jb] / a[ib]):
        ib, jb = im, j
if ib and jb:
    print(ib + 1, jb + 1)
else:
    print(0, 0)
