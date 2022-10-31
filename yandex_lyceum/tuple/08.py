# Сортировка в обратном порядке
n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(n - 1):
    for j in range(i, n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print('\n'.join(map(str, a)))
