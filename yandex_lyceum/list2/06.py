# Электрическая кошка
m, n, x, y, f = (int(input()) for _ in range(5))
a = [[0] * m for _ in range(n)]
a[y][x] = f
if f == 1:
    for row in a:
        print(*row, sep='\t')
    exit(0)
for i in range(n):
    for j in range(m):
        k = max(abs(i - y), abs(j - x))
        t = f
        for q in range(k):
            t = int(t ** .5)
        t1 = t
        for q in range(k):
            t1 = t1 ** 2
        if t1 != f:
            a[i][j] = 0
        else:
            a[i][j] = t
for row in a:
    print(*row, sep='\t')
