# Считать и отсортировать таблицу
n = int(input())
m = int(input())
a = []
for i in range(n):
    row = [input() for __ in range(m)]
    if i not in (0, n - 1):
        row.sort()
    a.append(row)
    print('\t'.join(row))
