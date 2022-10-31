# Крупные города
from sys import stdin

data = stdin.readlines()
d = {}
for x in data:
    town, tmp, count = x.split()
    key = int(count[:-5] + '00')
    d[key] = d.get(key, []) + [town]
for x in sorted(d.keys()):
    print(f'{x} - {x + 100}: {", ".join(sorted(d[x]))}')
