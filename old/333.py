print(50 % 18)
print(50 % 9)
print(50 % 6)
for i in range(50 // 18):
    for j in range(50 // 9):
        for k in range(50 // 6):
            if 18 * i + 9 * j + 6 * k == 51:
                print(i, j, k)
