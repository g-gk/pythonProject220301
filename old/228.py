n, a, k = [int(input()) for _ in range(3)]
print((n - n // k) * a)
print(sum(a for i in range(n) if (i + 1) % k))
s = 0
for i in range(n):
    if (i + 1) % k:
        s += a
print(s)
