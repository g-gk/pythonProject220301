for a in range(1, 500):
    b = 500 - a
    sab = 1000 * a * b
    for na in range(100):
        for nb in range(100):
            a1 = na * a + nb * b
            if a1 > 550:
                break
            for ma in range(100):
                for mb in range(100):
                    b1 = ma * a + mb * b
                    sa1b1 = a1 * b1
                    if a1 + b1 > 550 or sa1b1 > sab:
                        break
                    elif a1 + b1 == 550 and sa1b1 == sab:
                        print(na, nb, ma, mb)
                        exit(0)
