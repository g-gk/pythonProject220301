# Великолепные холмы
from sys import stdin

lines = list(map(str.strip, stdin.readlines()))
res1, res2 = set(), set()
for i in range(len(lines)):
    if i % 2:
        res2 = res2 | set(x for x in lines[i].split() if x[0] == x[0].upper())
    else:
        res1 = res1 | set(lines[i].split())
print('; '.join(res1))
print('; '.join(res2))
