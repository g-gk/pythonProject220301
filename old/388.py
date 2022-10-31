# Факториал
# Для заданного натурального N найти последнюю ненулевую цифру числа N!.
n = int(input())
ans = 1
n2, n5 = 0, 0
for i in range(1, n + 1):
    p = i
    while p % 2 == 0:
        p //= 2
        n2 += 1
    while p % 5 == 0:
        p //= 5
        n5 += 1
    ans *= p
    ans %= 10
if n2 > n5:
    ans *= 2 ** (n2 - n5)
elif n5 > n2:
    ans *= 5
print(ans % 10)
