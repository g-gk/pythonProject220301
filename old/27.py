def check_pin(pinCode):
    # разделяем пинкод нав числа a, b, c
    a, b, c = pinCode.split('-')
    # создаем флажки для проверки a, b, c
    fa, fb, fc = True, True, True
    # проверяем, является ли а простым, с помощью подсчета делителей
    a = int(a)
    number_of_dividers = 0
    for i in range(1, a + 1):
        if a % i == 0:
            number_of_dividers = number_of_dividers + 1
    # если число делителей не равно 2, то число не простое
    if number_of_dividers != 2:
        fa = False
    # проверяем, является ли b палиндромом с помощью метода reversed
    reversed_b = ''.join(reversed(b))
    if reversed_b != b:
        fb = False
    # проверяем, является ли c - степенью двойки
    c = int(c)
    i = 1
    while i < c:
        i = i * 2
    if i != c:
        fc = False
    # проверяем, все ли элементы подходят под условие
    if fa and fb and fc:
        return 'Корректен'
    # в обратном случае
    else:
        return 'Некорректен'


print(check_pin('7-101-4'))
print(check_pin('12-22-16'))
