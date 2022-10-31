# Сложность двоичного поиска
n = int(input()) - 1
ans = 0
while n > 0:
    n //= 2
    ans += 1
print(ans)
