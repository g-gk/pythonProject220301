# Поменять местами две диагонали
# Дан квадратный массив. Поменяйте местами в каждом столбце элементы,
# стоящие на главной и побочной диагонали.
n = int(input())
a = [input().split() for _ in range(n)]
for i in range(n):
    a[i][i], a[n - i - 1][i] = a[n - i - 1][i], a[i][i]
for r in a:
    print(*r)