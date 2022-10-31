a = []
b = input()


def check_password(func):
    def qwer(n):
        if len(a) == 0:
            d = input('пароль: ')
            if d != b:
                print('В доступе отказано')
                return None
            if d == b:
                a.append(1)
                return func(n)
        else:
            return func(n)

    return qwer


@check_password
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))
