from math import gcd

for a in range(123, 1000000):
    b = a ** 2 + 1
    if gcd(a, b) > 1:
        print(a, b)
