# Факториал
# Для заданного натурального N найти последнюю ненулевую цифру числа N!.
from math import factorial

n = int(input())
ans = factorial(n)
while ans % 10 == 0:
    ans //= 10
print(ans % 10)
