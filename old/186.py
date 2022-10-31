def eratosthenes(n):
    pl = []
    pl1 = []

    if n < 4:
        return

    for i in range(2, n + 1, 1):
        pl.append(i)

    while pl:
        for i in pl[1:]:
            if i % pl[0] == 0:
                pl1.append(i)
                pl.remove(i)
        pl = pl[1:]

    for i in pl1:
        print(i, end=" ")


eratosthenes(8)
