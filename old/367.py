# Носки
L, n, m = list(map(int, input().split()))
cnt = [0] * (L + 1)
for _ in range(n):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        cnt[i] += 1
for i in range(m):
    print(cnt[int(input())])
