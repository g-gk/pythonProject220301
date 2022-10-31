# Треугольники
from bisect import *
from sys import stdin

data = list(map(int, stdin))
n = data[0]
data = sorted(data[1:])
cnt = 0
for i in range(n - 2):
    a = data[i]
    for j in range(i + 1, n - 1):
        b = data[j]
        mx = a + b
        bl = bisect_left(data, mx)
        if bl > j:
            cnt += bl - j - 1
print(cnt)
