import functools
import sys

words = map(str.strip, sys.stdin)
print(words)
print(functools.reduce(lambda result, element:
                       element if (element == sorted([element, result])[0]) else result, words))
