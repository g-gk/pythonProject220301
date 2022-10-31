# Полумагический квадрат
from sys import stdin

data = stdin.readlines()
data = [list(map(int, x.split())) for x in data]
sum_rows = (sum(row) for row in data)
sum_cols = (sum(col) for col in zip(*data))
print('YES' if all(x[0] == x[1] for x in zip(sum_rows, sum_cols)) else 'NO')
