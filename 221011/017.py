# D. Уродливость гистограммы
t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]+list(map(int, input().split()))+[0]
    if n == 1:
        print(a[0])
        continue
    u = a[0] + a[-1]
    for i in range(n - 1):
        u += abs(a[i] - a[i + 1])
    # print(u)
    um = u

    ok = True
    while ok:
        u0 = u
        while a[0] > a[1]:
            a[0] -= 1
            u -= 1
        while a[n - 1] > a[n - 2]:
            a[n - 1] -= 1
            u -= 1
        for i in range(2, n - 1):
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                a[i] -= 1
                u -= 1
        um = min(um, u)
        if u0 == um:
            ok = False
        # print(*a)
    print(um)
