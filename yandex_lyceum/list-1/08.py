# Экономия
n = int(input())
t = [[0] * n for _ in range(n)]
for i in range(n - 1):
    row = input().split()
    for j in range(len(row)):
        t[i + 1][j] = int(row[j])
        t[j][i + 1] = int(row[j])
# print()
# print('\n'.join('\t'.join(map(str, row)) for row in t))
a, b = map(int, input().split())
mn = t[a][b]
# print(mn)
ans = a
for i in range(n):
    if i != b and i != a:
        st = t[a][i] + t[i][b]
        if st < mn:
            ans = i
            mn = st
print(ans)
