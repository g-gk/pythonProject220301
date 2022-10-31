# Разделение королевства
from sys import stdin

data = stdin.readlines()
n = int(data[0])
a = sorted(tuple(map(int, x.split())) for x in data[1:])
sx = set()
sy = set()
for i in range(n - 1):
    if a[i + 1][0] == a[i][0]:
        sy.add(a[i][1] + 1)
    else:
        sx.add(a[i][0] + 1)
ans = [f'y {y}' for y in sy] + [f'x {x}' for x in sx]
print('\n'.join([str(len(ans))] + ans))
