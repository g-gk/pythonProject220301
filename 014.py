n = 4567
for _ in range(2021):
    if n % 3 == 0:
        n -= 1
    elif n % 3 == 1:
        n += 2
    elif n % 3 == 2:
        n -= 2
print(n)  # 1539

