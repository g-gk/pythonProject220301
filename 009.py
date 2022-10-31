ss = '0123456789'
for x in range(2, 99):
    sx = str(x)
    y = 100 - x
    sy = str(y)
    cnt = [0] * 10
    s1 = sx * x + sy * y + str(x - 2) * y + str(y - 2) * x
    for c in s1:
        cnt[ss.index(c)] += 1
    for i in range(10):
        if cnt[i] > 222:
            print(x, y, i, cnt[i])
    cnt = [0] * 10
    s1 = sx * x + sy * y + str(x + 2) * y + str(y - 2) * x
    for c in s1:
        cnt[ss.index(c)] += 1
    for i in range(10):
        if cnt[i] > 222:
            print(x, y, i, cnt[i])
    cnt = [0] * 10
    s1 = sx * x + sy * y + str(x - 2) * y + str(y + 2) * x
    for c in s1:
        cnt[ss.index(c)] += 1
    mx = max(cnt)
    for i in range(10):
        if cnt[i] > 222:
            print(x, y, i, cnt[i])
    cnt = [0] * 10
    s1 = sx * x + sy * y + str(x + 2) * y + str(y + 2) * x
    for c in s1:
        cnt[ss.index(c)] += 1
    for i in range(10):
        if cnt[i] > 222:
            print(x, y, i, cnt[i])

# 9 91 1 273
# 34 66 6 232
