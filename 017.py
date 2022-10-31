cnt = 0
for n in range(1, 2022):
    if (n ** n + (2020 - n) ** (2021 - n)) % 3 == 0:
        cnt += 1
print(cnt)  # 674
