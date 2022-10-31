# Свернуть к минимуму
from functools import reduce
from sys import stdin

words = stdin.readlines()
print(reduce(lambda x, y: min(x, y), words))
