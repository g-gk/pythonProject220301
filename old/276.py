# Шахматная доска
# Поле шахматной доски определяется парой натуральных чисел, каждое из которых не превосходит 8. По
# введенным координатам двух полей (k,l) и (m,n) выясните, являются ли эти поля полями одного цвета?
k = int(input())
l = int(input())
m = int(input())
n = int(input())
if (k + l) % 2 == (n + m) % 2:
    print('YES')
else:
    print('NO')
