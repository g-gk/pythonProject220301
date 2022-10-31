# Радиоактивная порода
dt2 = input().split()
elements = input().split()
n = len(elements)
t2 = {}
for i in range(0, len(dt2), 2):
    t2[dt2[i]] = int(dt2[i + 1])
r = list(map(float, input().split()))
dop = float(input())
d = 0
total = sum(r)
while total > dop:
    d += 1
    total = sum(r[i] / 2 ** (d // t2[elements[i]]) for i in range(n))
print(d)
print(*(r[i] / 2 ** (d // t2[elements[i]]) for i in range(n)))
