# Шляпа
n, m = map(int, (input().split()))
w = {}
cnt = [0] * n
for _ in range(m):
    x = input().split()
    w[x[1]] = int(x[0])
for k, v in w.items():
    cnt[v - 1] += 1
print(*cnt)
