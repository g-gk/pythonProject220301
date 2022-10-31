# Большое число
n = int(input())
a = [input() for i in range(n)]
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] + a[j + 1] < a[j + 1] + a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(''.join(a))
