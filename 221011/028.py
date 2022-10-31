a = [[], [], []]
a[0] = list(map(int, '2 3 4 5 6'.split()))
a[1] = list(map(int, '2 3 4 5 6 7'.split()))
a[2] = list(map(int, '2 3 4 5 6 7 8'.split()))
for x in a:
    n = len(x)
    x.sort()
    s = 0
    mx = 0
    for i in range(n):
        res = sum(x[:i]) * sum(x[i:])
        mx = max(mx, res)
    print(mx)
