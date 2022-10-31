# Отрезок
from math import gcd

a, b, c, d = map(int, input().split())
g = gcd(abs(c - a), abs(d - b))
print(abs(c - a) + abs(d - b) - g)
