# Разделение королевства
sx, sy, xx, yy = set(), set(), set(), set()
n = int(input())
mx,my = '',''
for _ in range(n):
    x, y = input().split()
    sx.add(x)
    sy.add(y)
    if x in sx:
        yy.add(y)
    if y in sy:
        xx.add(x)
print('x', *(int(x) + 1 for x in xx))
print('y', *(int(y) + 1 for y in yy))
