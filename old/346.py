# Ходы коня
# На шахматной доске стоит конь. Отметьте положение коня на доске и все клетки, которые он
# бьёт. Клетку, где стоит конь, отметьте английской буквой «K». Клетки, которые он бьёт,
# отметьте символами «*». Остальные клетки заполните точками.
n = 8
r, c = map(int, input().split())
a = [['.'] * n for _ in range(n)]
a[r - 1][c - 1] = 'K'
for i, j in ((-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)):
    if 0 < r + i < 9 and 0 < c + j < 9:
        a[r + i - 1][c + j - 1] = '*'
for row in a:
    print(*row)