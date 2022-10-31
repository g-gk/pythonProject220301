# D. Оракул
n = int(input())
a = []
for i in range(n):
    name, *b = input().split()
    sumb = sum(map(int, b))
    a.append([sumb, name])
ans = []
for el in a:
    b = [(-x[0] - 500, x[1]) if x[1] == el[1] else (-x[0], x[1]) for x in a]
    b = sorted(b)
    # print(b)
    for i in range(n):
        if b[i][1] == el[1]:
            ans.append([i + 1])
for j in range(n):
    el = a[j]
    c = [(-x[0], x[1]) if x[1] == el[1] else (-x[0] - 500, x[1]) for x in a]
    c = sorted(c)
    # print(c)
    for i in range(n):
        if c[i][1] == el[1]:
            ans[j].append(i + 1)
for elm in ans:
    print(*elm)
