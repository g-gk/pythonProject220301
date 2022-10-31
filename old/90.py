def w(n):
    d = 2
    while n % d != 0 and d * d <= n:
        d += 1
    return n > 1 and d * d > n


def palindrom(string):
    return str(string)[::-1] == str(string)


def pow(n):
    return bin(n).count('1') == 1


def check_pin(str):
    x = [int(i) for i in str.split('-')]
    if (w(x[0]) and pow(x[2])) and palindrom(x[1]):
        return 'Корректен'
    else:
        return 'Некорректен'


print(check_pin('7-101-4'))
