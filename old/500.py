# Разделение королевства
from sys import stdin

data = stdin.readlines()
n = int(data[0])
points = data[1:]
sx = set()
sy = set()
mxx, mxy = 0, 0
for i in range(n):
    x, y = map(int, points[i].split())
    if i == 0 or x > mxx:
        mxx = x
    if i == 0 or y > mxy:
        mxy = y
    sx.add(x)
    sy.add(y)
sx.remove(mxx)
sy.remove(mxy)

ans = []
if sx:
    ans += [f'x {x + 1}' for x in sx]
if sy:
    ans += [f'y {y + 1}' for y in sy]
print(len(ans))
print('\n'.join(ans))
