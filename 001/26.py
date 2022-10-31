with open('26.txt') as f:
    data = f.readlines()
n = int(data[0])
koord = [tuple(map(int, r.split())) for r in data[1:]]
t = [[0] * n for _ in range(n)]
for k in koord:
    t[k[0] - 1][k[1] - 1] = 1
t1 = [sum(r[1::2]) for r in t]
mxp = max(t1)
mnr = t1.index(mxp) + 1
print(mxp, mnr)
