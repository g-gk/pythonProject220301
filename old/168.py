import sys

d = sys.stdin.read()
print(d)
print(any(["0" in i.split() for i in d]))
