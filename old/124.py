# J. Футболки
from sys import stdin


def dfs(v):
    global used
    used[v] = True
    for u in di[v]:
        if used[u]:
            continue
        dfs(u)


data = list(map(str.strip, stdin))
n, m, q = map(int, data[0].split())
di = {i: set() for i in range(n)}
for i in range(m):
    p = list(map(int, data[1 + i].split()))
    for j in range(n):
        di[j].add(p[j] - 1)
test = [[False for _ in range(n)] for __ in range(n)]
for i in range(n):
    used = test[i]
    dfs(i)
print(test)
ans = ['NO' for _ in range(q)]
for i in range(q):
    a, b = map(int, data[m + i + 1].split())
    if test[a - 1][b - 1]:
        ans[i] = 'YES'
print('\n'.join(ans))
