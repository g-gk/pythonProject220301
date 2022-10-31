# Считать и вывести таблицу — 3
n = int(input())
m = int(input())
a = []
for r in range(n):
    a.append([input() for _ in range(m)])
    print('\t'.join(a[-1]))
