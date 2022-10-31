# Диофантово уравнение
from math import gcd

a, b, c = map(int, input().split())
d = gcd(a, b)
if c % d:
    print(-1)
else:
    for x in range(10000000):
        y = (c - a * x) / b
        if y == int(y):
            print(x, int(y))
            break
