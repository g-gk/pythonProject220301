# Делёж яблок — 2
n = int(input())
k = int(input())
print((n - (k - k // n * n)) % n)
