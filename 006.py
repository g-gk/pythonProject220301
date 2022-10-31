for i in range(0, 1000, 2):
    a = i
    x = 0
    while a >= 0:
        a -= 2
        x += 1
    if x == 6:
        print(i)
        break
