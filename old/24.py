s1, s2 = 0, 0
ds1, ds2 = 72, 60
count = 0
i = 0
while count < 901:
    if i % 60 == 0 and i % 72 == 0:
        count += 1
    i += 1
i -= 1
print(i / 60, i / 72)
print(i / 100)  # 3.24
