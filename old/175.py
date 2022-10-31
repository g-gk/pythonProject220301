from functools import reduce
from math import gcd
import sys

data = list(map(int, sys.stdin))
print(reduce(lambda x, y: gcd(x, y), data))
