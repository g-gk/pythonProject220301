a, b, c = 36, -4, 5
res = (a - b) * c + b * c - (a + b * c ** 2) * (a + b + 1)
print(res)
print(res % 11)
