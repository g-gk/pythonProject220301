# Треугольники

from sys import stdin

data = list(map(int, stdin))
n = data[0]
data = data[1:]
cnt = 0
for i in range(n - 2):
    a = data[i]
    for j in range(i + 1, n - 1):
        b = data[j]
        for k in range(i + j + 1, n):
            c = data[k]
            if a + b > c and a + c > b and b + c > a:
                cnt += 1
print(cnt)
