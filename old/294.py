# Количество нулей
# Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.
n = int(input())
cnt = 0
for x in range(n):
    if input() == '0':
        cnt += 1
print(cnt)
