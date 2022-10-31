# Сумма в виде Н
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(1, n - 1):
    for j in range(1, n - 1):
        s = 0
        for k in range(i - 1, i + 2):
            s += sum(a[k][j - 1:j + 2])
        s = s - a[i - 1][j] - a[i + 1][j]
        if i + j == 2 or s > mx:
            mx = s
print(mx)
