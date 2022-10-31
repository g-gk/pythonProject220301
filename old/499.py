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
    mx = max(mx, x)
    my = -10 ** 10
    for y in p[x]:
        my = max(my, y)
        yy.add(y)
    yy.remove(my)
    xx.add(x)
xx.remove(mx)
ans = [f'x {x + 1}' for x in xx] + [f'y {y + 1}' for y in yy]
print('\n'.join([str(len(ans))] + ans))
