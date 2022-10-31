# Минимальный простой делитель
# Дано целое число, не меньшее 2. Выведите его наименьший простой делитель.
n = int(input())
if n % 2 == 0:
    ans = 2
else:
    d = 3
    while n % d != 0 and d ** 2 <= n:
        d += 2
    if n % d == 0:
        ans = d
    else:
        ans = n
print(ans)
