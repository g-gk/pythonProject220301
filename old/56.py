# Таблица квадратов
def squared(a, b, k):
    table = ''
    for i in range(a, b + 1):
        if i ** 2 % k != 0:
            table += f"{i ** 2:<5}"
        if (i + 1) % 10 == a % 10:
            table += '\n'
    print(table)


squared(11, 99, 10)
squared(4, 33, 9)
