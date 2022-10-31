# Поменять столбцы
# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j.
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
i, j = map(int, input().split())
for row in a:
    row[i], row[j] = row[j], row[i]
    print(*row)
