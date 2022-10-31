# B. Смертоносный лазер
t = int(input())
for _ in range(t):
    n, m, sx, sy, d = map(int, input().split())
    if sx + d >= n and sy + d >= m:
        print(-1)
    elif sx + d >= n and sx - d <= 1:
        print(-1)
    elif sy + d >= m and sy - d <= 1:
        print(-1)
    elif n == 1 or m == 1:
        print(-1)
    elif sx - d <= 1 and sy - d <= 1:
        print(-1)
    else:
        print(n + m - 2)
