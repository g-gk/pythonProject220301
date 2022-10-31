# Разложение на чётнопростые


def f(n):
    if n == 1:
        return True, 1, 1
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False, d, n // d
        d += 1
    return True, 1, 1


for i in range(4, 8, 4):
    n = int(input())
    # n = i
    # print(n)
    n2 = 0
    if n % 4:
        print('prime')
    else:
        f1, a, b = f(n // 4)
        if f1:
            print('single')
            print(2, n // 2)
        else:
            print('many')
            print(2, n // 2)
            print(2 * a, n // 2 // a)
