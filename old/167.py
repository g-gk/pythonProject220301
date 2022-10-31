import sys

data = sys.stdin.read()
count = list(map(lambda x: x.lstrip().startswith("#"), data.split("\n"))).count(True)
print(count)
