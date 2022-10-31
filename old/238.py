from math import gcd

n, a, b = [int(input()) for _ in range(3)]
print(n // a + n // b - n // (a * b // gcd(a, b)))
