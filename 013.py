cnt = 0
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if x + y + z == 6:
                cnt += 1
                print(cnt, x, y, z)
