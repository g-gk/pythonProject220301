# Треугольник Паскаля
# Даны два числа n и m. Создайте массив n×m и заполните его по следующим правилам:
# Числа, стоящие в строке 0 или в столбце 0 равны 1 (A[0][j] = 1, A[i][0] = 1).
# Для всех остальных элементов массива A[i][j] = A[i-1][j] + A[i][j-1], то есть каждый
# элемент равен сумме двух элементов, стоящих слева и сверху от него.
n, m = map(int, input().split())
a = [[1] * m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] = a[i - 1][j] + a[i][j - 1]
for r in a:
    print(*r, sep='\t')