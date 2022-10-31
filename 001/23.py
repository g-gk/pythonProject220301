n = 12
a = [[0, 0] for _ in range(n)]
print(a)
a[1] = [1, 0]
for i in range(2, n):
    a[i][0] = a[i - 1][0]
    if i % 2 == 0 and a[i // 2][1] < 2:
        a[i][0] += a[i // 2][0]
        a[i][1] = a[i // 2][1] + 1
    print(a[i])
print(a)
print(a[11][0])
