# Стильная одежда
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
i, j, ib, jb = 0, 0, 0, 0
while i < n and j < m:
    if abs(a[i] - b[j]) < abs(a[ib] - b[jb]):
        ib, jb = i, j
    if a[i] <= b[j]:
        i += 1
    else:
        j += 1
print(a[ib], b[jb])
