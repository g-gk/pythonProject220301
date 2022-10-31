# Проверка числа на простоту
x = int(input())
for d in range(2, int(x ** 0.5) + 1):
    if x % d == 0:
        print(d)
        exit(0)
print(x)
