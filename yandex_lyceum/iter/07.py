# Наибольший общий делитель
from math import gcd
from functools import reduce
from sys import stdin

numbers = map(int, stdin.readlines())
print(reduce(gcd, numbers))
