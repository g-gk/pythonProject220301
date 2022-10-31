# Разделение королевства
sdx = {}
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if x in sdx:
        sdx[x] += [y]
    else:
        sdx[x] = [y]
yy = []
xx = []
for k in sorted(sdx.keys()):
    if len(sdx[k]) > 1:
        for x in sorted(sdx[k])[:-1]:
            yy += ['y ' + str(x + 1)]
    xx += ['x ' + str(k)]
print(len(xx) + len(yy))
print('\n'.join(yy))
print('\n'.join(xx))
