# J. Футболки
import sys


def dfs(v):
    global used
    used[v] = True
    for u in di[v]:
        if used[u - 1]:
            continue
        dfs(u - 1)


data = list(map(str.strip, sys.stdin))
# n, m, q = map(int, input().split())
n, m, q = map(int, data[0].split())
di = {}

for j in range(n):
    di[j] = set()
for i in range(m):
    p = list(map(int, data[1 + i].split()))
    for j in range(n):
        di[j].add(p[j])

test = [[False for _ in range(n)] for __ in range(n)]

for i in range(n):
    used = test[i]
    dfs(i)

# print(test)
ans = ['NO' for _ in range(q)]
# print(ans)
for i in range(q):
    a, b = map(int, data[m + i + 1].split())
    if test[a - 1][b - 1]:
        # print('YES')
        ans[i] = 'YES'
    # else:
    #     print('NO')
print('\n'.join(ans))
