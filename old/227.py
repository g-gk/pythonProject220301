for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            t = x + y + z
            if ((40 <= t + z <= 49) and
                    (60 <= t + x <= 69) and
                    (20 <= y + 3 * z <= 29) and
                    (60 <= 3 * x + z <= 69)):
                print(x, y, z, t)
