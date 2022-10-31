for n in range(9999, 1000, -1):
    if len(set(str(n))) == 4:
        d = list(map(int, str(n)))
        if sum(d) == 16:
            if (abs(d[0] - d[1]) > 1 and abs(d[0] - d[2]) > 1 and abs(d[0] - d[3]) > 1 and
                    abs(d[1] - d[2]) > 1 and abs(d[1] - d[3]) > 1 and abs(d[2] - d[3]) > 1):
                print(n)
                break
# 9520
