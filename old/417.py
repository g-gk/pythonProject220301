from math import factorial


# Функция факторизации, то есть разложения на простые множители
def factor(n):
    res = []
    i = 2
    while i * i <= n:  # Ищем только до корня из n
        if n % i == 0:
            res.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        res.append(n)
    return res


n = int(input())
if n == 1:  # Факторизация единицы ничего не даст, обработаем её отдельно
    print(1)
else:
    primes = factor(factorial(n))  # Рассчитываем факториал и получаем все простые делители
    # Наш ответ будем умножать в процессе, поэтому 1
    # num отвечает за количество повторений актуального простого делителя
    # последний обработанный простой делитель, начинаем с первого элемента
    answer, num, actual, length = 1, 1, primes[0], len(primes)
    for i in range(1, length):  # Начинаем с 1, тк 0 элемент мы уже обработали
        if primes[i] == actual:  # Если такой уже был, то просто увеличиваем счетчик
            num += 1
        else:  # Если это новый простой делитель
            answer *= num + 1  # домножаем ответ на инкрементированное кол-во одинаковых делителей
            num = 1  # Обработка происходит уже на новом элементе, учитываем его
            actual = primes[i]  # Меняем текущий элемент
    answer *= num + 1  # Последняя обработка не попадет в цикл, домножим так
    print(answer)