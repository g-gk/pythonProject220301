# Большое число
from random import randint

# n = int(input())
n = randint(1, 10)
# a = [input().strip() for _ in range(n)]
a = [''.join(str(randint(0, 2)) for __ in range(randint(1, 10))) for _ in range(n)]
print(' '.join(a))
b = sorted(a, key=lambda x: (int(x) != 0, x + '9' * (100 - len(x))), reverse=True)
print(' '.join(b))
c = a[::]
for i in range(n):
    for j in range(n - 1 - i):
        if c[j] + c[j + 1] < c[j + 1] + c[j]:
            c[j], c[j + 1] = c[j + 1], c[j]
print(' '.join(c))
