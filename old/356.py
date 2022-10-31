# Заполнение змейкой
# По данным числам n и m заполните двумерный массив размером n×m числами
# от 1 до n⋅m «змейкой», как показано в примере.
n, m = map(int, input().split())
a = [[m * (i + 1) - j if i % 2 else m * i + (j + 1) for j in range(m)] for i in range(n)]
for row in a:
    print(*row, sep='\t')
