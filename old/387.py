# Факториал
# Для заданного натурального N найти последнюю ненулевую цифру числа N!.
from math import factorial

# n = int(input())
for j in range(10000):
    n = j
    ans = 1
    n2, n5 = 0, 0
    for i in range(1, n + 1):
        ans *= i
        while ans % 2 == 0:
            ans //= 2
            n2 += 1
        while ans % 5 == 0:
            ans //= 5
            n5 += 1
        # ans %= 10
    # print(ans)
    if n2 > n5:
        ans *= 2 ** (n2 - n5) % 10
    elif n5 > n2:
        ans *= 5 % 10
    ans = ans % 10
    ans2 = factorial(n)
    while ans2 % 10 == 0:
        ans2 //= 10
    if ans != ans2 % 10:
        print(n, ans, ans2)
        # break
