# Проверка чека
n, total = map(int, input().split())
ans = []
d = 0
for i in range(n):
    x = input().split()
    t = int(x[0]) * int(x[1][1:])
    y = int(x[2][1:]) - t
    d += t
    if y:
        ans += [i + 1]
print(total - d)
if d:
    print(*ans)
