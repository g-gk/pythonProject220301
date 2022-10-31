from functools import reduce
import sys

data = [i.replace("/n", "") for i in map(str.strip, sys.stdin)]
print(reduce(lambda x, y: sorted([x, y])[0], data))
