# Красота превыше всего
n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    print(1, 1)
    exit(0)
cnt = [0] * (k + 1)
ib, jb = 0, 1
cnt[a[ib]], d = 1, 0
while d < k - 1:
    if cnt[a[jb]] == 0:
        d += 1
    cnt[a[jb]] += 1
    jb += 1
jb -= 1
i, j = ib, jb
while i < n and j < n:
    if cnt[a[i]] > 1:
        cnt[a[i]] -= 1
        i += 1
        if j - i < jb - ib:
            ib, jb = i, j
    else:
        if j < n - 1:
            j += 1
            cnt[a[j]] += 1
        else:
            break
print(ib + 1, jb + 1)
