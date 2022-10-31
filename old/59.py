import functools
from sys import stdin
from math import gcd

a = []
for b in stdin:
    a.append(int(b.split('\n')[0]))

# print(functools.reduce(gcd, a, max(a)))
print(functools.reduce(gcd, a))
