# Выборы в США
n = int(input())
d1 = {}
for _ in range(n):
    x = input().split()
    d1[x[0]] = d1.get(x[0], 0) + int(x[1])
m = int(input())
d2 = {}
for _ in range(m):
    x = input().split()
    if x[0] in d2:
        if x[1] in d2[x[0]]:
            d2[x[0]][x[1]] += 1
        else:
            d2[x[0]][x[1]] = 1
    else:
        d2[x[0]] = {x[1]: 1}
names = {}
for key in d2:
    mx, name = 0, ''
    for k, v in d2[key].items():
        names[k] = names.get(k, 0)
        if v > mx or v == mx and k < name:
            mx, name = v, k
    names[name] = names.get(name, 0) + d1[key]
ans = sorted(names.items(), key=lambda x: (-x[1], x[0]))
for el in ans:
    print(*el)
