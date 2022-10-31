import random

n = 5000000
n1 = 0.0
for i in range(n):
    x = random.random()
    y = random.random()
    n1 += (x * x + y * y <= 1.0)
print(4 * n1 / n)
