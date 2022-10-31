# E. Пол — это лава!
a, b, n = map(int, input().split())
print((n - a + b - a - 1) // (b - a) + (n - b + b - a - 1) // (b - a))
