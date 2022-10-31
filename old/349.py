# Максимум
# Найдите индексы первого вхождения максимального элемента в двумерном массиве.
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
im, jm = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] > a[im][jm]:
            im, jm = i, j
print(im, jm)
