# Модные средние в статистике
a = sorted(map(int, input().split()))
n = len(a)
cur = a[0]
cnt = 1
moda = a[0]
mx = 1
for i in range(1, n):
    if a[i] == a[i - 1]:
        cnt += 1
    else:
        if cnt > mx:
            mx = cnt
            moda = cur
        cur = a[i]
        cnt = 1
if cnt > mx:
    mx = cnt
    moda = cur
print(a[n // 2], moda)
