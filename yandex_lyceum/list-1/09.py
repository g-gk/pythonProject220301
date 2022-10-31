# Где экономия?
n = int(input())
t = [[0] * n for _ in range(n)]
for i in range(n - 1):
    row = input().split()
    for j in range(len(row)):
        t[i + 1][j] = int(row[j])
        t[j][i + 1] = int(row[j])
# print()
# print('\n'.join('\t'.join(map(str, row)) for row in t))
ans = []
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(n):
            if k != i and k != j:
                st = t[i][k] + t[k][j]
                if st < t[i][j]:
                    ans.append((i, j))
                    break
for x in sorted(ans):
    print(*x)
