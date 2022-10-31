# Сумма, делящаяся на три
n = int(input())
a = list(map(int, input().split()))
p = 0
ib, jb = [-1] * 3, [-1] * 3
for i in range(n):
    p += a[i]
    p %= 3
    if p == 0:
        ib[0] = 0
        jb[0] = i
    elif ib[p] < 0:
        ib[p] = i
    else:
        jb[p] = i

if jb[0] >= 0:
    ans = [1, jb[0] + 1]
    mx = jb[0]
else:
    ans = [-1]
    mx = -1
for i in range(1, 3):
    # print(ib[i], jb[i])
    if ib[i] >= 0 and jb[i] >= 0:
        if jb[i] - ib[i] - 1 > mx or jb[i] - ib[i] - 1 == mx and ib[i] < ans[0] - 1:
            ans = [ib[i] + 2, jb[i] + 1]
            mx = jb[i] - ib[i]
print(*ans)
