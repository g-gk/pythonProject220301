n = 102
a = [[0] * n for _ in range(n)]
a[1][1] = 1
day = 1
print(day)
for r in a[1:10]:
    print(*r[1:10])
for day in range(2, 1000):
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            a[i][j] += (a[i - 1][j] > 0) + (a[i + 1][j] > 0) + (a[i][j - 1] > 0) + (
                    a[i][j + 1] > 0)
            if i + j > day:
                break
        if i > day - 1:
            break
    if a[50][50] > 10:
        print(day)
        for r in a[1:51]:
            print(*r[1:51], sep='\t')
        break
