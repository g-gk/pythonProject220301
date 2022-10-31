# Простое число
n = 2_000_000
t = [i for i in range(n + 1)]
t[:2] = [0, 0]
for i in range(2, n + 1):
    if t[i]:
        for j in range(i ** 2, n + 1, i):
            t[j] = 0
primes = [i for i in t if i]
print(len(primes))
k = int(input())
print(primes[k - 1])
