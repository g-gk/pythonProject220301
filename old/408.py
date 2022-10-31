# Обратное число
from math import gcd


def pow(a, n, m):
    if n == 1:
        return a % m
    if n % 2:
        return a * pow(a, n - 1, m) % m
    return pow(a, n // 2, m) ** 2 % m


m, a = map(int, input().split())
t = m
if gcd(m, a) != 1:
    print(-1)
else:
    fm = m
    d = 2
    while d ** 2 <= m:
        if m % d == 0:
            fm -= fm // d
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fm -= fm // m
    print(pow(a, fm - 1, t))
