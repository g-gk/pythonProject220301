# Треугольник
# Вам даны 4 отрезка. Выведите YES, если среди них найдутся 3, из которых можно составить
# треугольник, и NO в противном случае.
# Для решения напишите функцию triangle(a, b, c), которая будет возвращать True,
# если из трёх заданных отрезков можно составить треугольник, и False иначе.
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


a, b, c, d = [int(input()) for _ in range(4)]
if triangle(a, b, c) or triangle(a, b, d) or triangle(a, c, d) or triangle(b, c, d):
    print('YES')
else:
    print('NO')
