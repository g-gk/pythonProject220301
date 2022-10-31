for i in range(1, 1000):
    d = i  # int(input())
    n = 3
    s = 38
    while s <= 1200:
        s += d
        n += 7
    # print(n)
    if n == 150:
        print(i)
