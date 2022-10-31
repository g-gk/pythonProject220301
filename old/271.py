# Симметричное число
n = int(input())
a, b, c, d = n // 1000, n % 1000 // 100, n % 100 // 10, n % 10
# print(a, b, c, d)
print((a - d) ** 2 + (b - c) ** 2 + 1)
