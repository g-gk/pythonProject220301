from math import gcd

ans = set()
for l in range(-10000, 10001):
    g = gcd(5 * l + 6, 8 * l + 7)
    if g > 1:
        ans.add(g)
print(*ans)
