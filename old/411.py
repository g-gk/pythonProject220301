# Разложение на чётнопростые


def f(n):
    if n == 1:
        return True, 0, 0
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False, d, n // d
        d += 1
    return True, 0, 0


for i in range(2, 100, 2):
    # n = int(input())
    n = i
    print(n)
    if n % 2 == 0:
        n1 = n // 2
        if n1 % 2 == 0:
            n2 = n1 // 2
            f1, a, b = f(n2)
            if f1:
                print('single')
                print(2, n1)
            else:
                print('many')
                print(2, n1)
                print(2 * a, n1 // a)
        else:
            print('prime')
    else:
        print('prime')
