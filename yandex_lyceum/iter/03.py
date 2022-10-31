# Полумагический квадрат
from sys import stdin

data = stdin.readlines()
# print(data)
# for row in data:
#     print(row)
# print(data)
data = [list(map(int, x.split())) for x in data]
# print(data)
# for row in data:
#     print(*row)
#
# for row in data:
#     print(*row)

sum_rows = (sum(row) for row in data)
sum_cols = (sum(col) for col in zip(*data))
# print(*sum_rows)
# print(*sum_cols)
# for x in zip(sum_rows, sum_cols):
#     print(x)
# for x in zip(sum_rows, sum_cols):
#     print(x)
# print(*(x[0] == x[1] for x in zip(sum_rows, sum_cols)))
print('YES' if all(x[0] == x[1] for x in zip(sum_rows, sum_cols)) else 'NO')
