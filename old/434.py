# Красота превыше всего
n, k = map(int, input().split())
a = list(map(int, input().split()))
ok = set(range(1, k + 1))
i, j, ib, jb = 0, 0, 0, n - 1
while i < n and j < n:
    if set(a[i:j + 1]) == ok:
        if j - i < jb - ib:
            ib, jb = i, j
        i += 1
    elif set(a[i:j + 1]) < ok:
        if j < n - 1:
            j += 1
        else:
            break
print(ib + 1, jb + 1)
