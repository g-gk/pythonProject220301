# Последовательность
n = int(input())
a = [i for i in range(1, n + 1)]
x = int(input())
n2 = 0
f = True
for i in range(1, n + 1):
    if f:
        if a[n2:n2 + x]:
            print(*a[n2:n2 + x], sep='\n')
            n2 = n2 + x
        f = False
    else:
        n2 += x
        f = True
