# Родословная
from sys import stdin


def h(m):
    if m not in pt:
        return 0
    return h(pt[m]) + 1


data = list(map(str.strip, stdin))
n = int(data[0])
pt = {}
for x in data[1:]:
    a, b = x.split()
    pt[a] = b
res = {}
for m in set(pt.keys() | pt.values()):
    res[m] = h(m)
for k in sorted(res):
    print(k, res[k])
