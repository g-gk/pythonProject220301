# Созвездия
n = int(input())
a = [[' '] * n for _ in range(n)]
i, j = 0, 6
li, ri, lj, rj = 2, n - 1, 0, n - 1
while True:
    while j >= lj:
        a[i][j] = '*'
        j -= 1
    j += 1
    lj += 2
    while i <= ri:
        a[i][j] = '*'
        i += 1
    i -= 1
    ri -= 2
    while j <= rj:
        a[i][j] = '*'
        j += 1
    j -= 1
    rj -= 2
    while i >= li:
        a[i][j] = '*'
        i -= 1
    i += 1
    li -= 2
    j -= 1
    if li <= i <= ri and lj <= j <= rj:
        a[i][j] = '*'
    else:
        break
    j -= 1
for row in a:
    print(' '.join(row))
print(i, j)
