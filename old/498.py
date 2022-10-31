# Разделение королевства
n = int(input())
p = {}
for _ in range(n):
    x, y = map(int, input().split())
    p[x] = p.get(x, []) + [y]
# print(p)
yy = set()
xx = []
for x in sorted(p.keys()):
    for y in sorted(p[x])[:-1]:
        yy.add(f'y {y + 1}')
    xx.append(f'x {x + 1}')

ans = list(yy) + xx[:-1]
print(len(ans))
print('\n'.join(ans))
