# Приближённый двоичный поиск
n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = []
for el in q:
    l1, r1 = -1, n
    while r1 - l1 > 1:
        m = (l1 + r1) // 2
        if a[m] <= el:
            l1 = m
        else:
            r1 = m
    if l1 == -1:
        ans += [a[0]]
    elif r1 == n:
        ans += [a[-1]]
    elif el - a[l1] <= a[r1] - el:
        ans += [a[l1]]
    else:
        ans += [a[r1]]
print(*ans, sep='\n')
