def f(x, div):
    if div < 0:
        return 0
    if x == 1:
        return 1
    if x % 2:
        return f(x - 1, div)
    return f(x - 1, div) + f(x // 2, div - 1)


print(f(11, 2))
