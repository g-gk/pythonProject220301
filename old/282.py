# Максимум трёх чисел
# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
# Использовать функции max и min, а также логические операции and и or нельзя.
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
