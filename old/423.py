# Клиппи и Мерлин грабят банк
n, k = map(int, input().split())
a = list(map(int, input().split()))
ib, jb, im = 0, k + 1, 0
for j in range(n - k - 1):
    if a[j] > a[im]:
        im = j
    if a[j + k + 1] + a[im] > a[jb] + a[ib]:
        ib, jb = im, j + k + 1
print(ib + 1, jb + 1)
