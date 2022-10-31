def squared(a, b, k):
    s = ''
    for i in range(a, b + 1):
        if i ** 2 % k != 0:
            s += str(i ** 2) + ' ' * (5 - len(str(i ** 2)))
        if (i + 1) % 10 == a % 10:
            s += '\n'
    print(s)


squared(11, 99, 10)
