# Тотальная децимация
n = int(input())
a = [input() for _ in range(n)]
k = int(input())
while a:
    for i in range(len(a)):
        d = []
        if i % k == 0:
            d += [i]
            print(a[i])
            a[i] = ''
    a = [x for x in a if x]
