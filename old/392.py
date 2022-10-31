# Upper bound
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
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
    ans += [r1]
print(*ans)
