# D. Уродливость гистограммы
t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    u = sum(abs(a[i] - a[i + 1]) for i in range(n + 1))
    # print(*a)
    # print(u)
    for i in range(1, n + 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            d = a[i] - max(a[i - 1], a[i + 1])
            a[i] -= d
            u -= d
    # print(*a)
    print(u)
