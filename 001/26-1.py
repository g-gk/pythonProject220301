with open('26.txt') as f:
    data = f.readlines()
n = int(data[0])  # 114091
koord = [tuple(map(int, r.split())) for r in data[1:]]
t = [0] * n
for k in set(koord):
    x, y = k
    if y % 2 == 0:
        t[x - 1] += 1
mxp = max(t)
mnr = t.index(mxp) + 1
print(mxp, mnr)  # 17 283
