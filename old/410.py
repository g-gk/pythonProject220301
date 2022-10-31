# Делители
from math import gcd

n = int(input())
t = n
divs = [1]
d = 2
while d <= n // 2:
    if t % d == 0:
        divs += [d]
    d += 1
divs += [n]
ans = 0
for i in range(len(divs) - 1):
    a = divs[i]
    for j in range(i + 1, len(divs)):
        b = divs[j]
        if gcd(a, b) == 1 and a * b <= n:
            ans += 1
print(ans)
