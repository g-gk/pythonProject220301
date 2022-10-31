from math import gcd

n = int(input())
d = set()

i = 1
while i ** 2 <= n:
    q, r = divmod(n, i)
    if r == 0:
        d.add(i)
        d.add(q)
    i += 1

d = list(sorted(d))
p = 0

for i in range(len(d) - 1):
    for j in range(i + 1, len(d)):
        if d[i] * d[j] > n:
            break
        if gcd(d[i], d[j]) == 1:
            p += 1

print(p)