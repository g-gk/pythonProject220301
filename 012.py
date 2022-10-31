for n in range(1, 200):
    for m in range(n + 1, 200):
        for x in range(1, n * m):
            if 8 * x + (n * m - 4 * x) * 2 == n * (m + 1) + m * (n + 1):
                print(n, m, x)
