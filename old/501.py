# Разделение королевства
from sys import stdin

data = stdin.readlines()
n = int(data[0])
points = data[1:]
p = {}
for i in range(n):
    x, y = map(int, points[i].split())
    p[x] = p.get(x, []) + [y]
# print(p)
yy = set()
xx = set()
mx = -10 ** 10
for x in p:
    y1 = set()
    my = -10 ** 10
    for y in p[x]:
        y1.add(y)
        my = max(my, y)
    y1.remove(my)
    yy |= y1
    xx.add(x)
    mx = max(mx, x)
# xx.remove(mx)
ans = [f'x {x + 1}' for x in xx if x != mx] + [f'y {y + 1}' for y in yy]
print(len(ans))
print('\n'.join(ans))
