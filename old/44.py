import functools
import sys
import math

words = map(int, sys.stdin)
print(functools.reduce(lambda result, element: math.gcd(result, element), words))
