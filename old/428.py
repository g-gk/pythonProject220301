# Сумма чисел в массиве
n = int(input())
a = [int(input()) for _ in range(n)]
p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i]
# print(p)
ib, jb, im = 0, 0, 0
for j in range(1, n):
    if p[j] <= p[im]:
        im = j
    if p[j + 1] - p[im] > p[jb + 1] - p[ib]:
        ib, jb = im, j
print(ib + 1)
print(jb + 1)
