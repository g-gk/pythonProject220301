# Красота превыше всего
n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (k + 1)
for x in a:
    cnt[x] += 1
i, j, ib, jb = 0, 0, 0, n - 1
oki, okj = True, True
while oki or okj:
    if cnt[a[i]] > 1:
        cnt[a[i]] -= 1
        i += 1
        if j - i < jb - ib:
            ib, jb = i, j
    else:
        oki = False
    if cnt[a[j]] < 1:
        if j<n-1:
            cnt[a[j]] += 1
            j += 1
            if j - i < jb - ib:
                ib, jb = i, j
        else:
            okj = False
print(ib + 1, jb + 1)
