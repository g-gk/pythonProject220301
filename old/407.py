# Функция Эйлера
n = int(input())
ans = n
d = 2
while d ** 2 <= n:
    if n % d == 0:
        ans -= ans // d
        while n % d == 0:
            n //= d
    d += 1
if n > 1:
    ans -= ans // n
print(ans)
