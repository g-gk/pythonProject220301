# Красота превыше всего
n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (k + 1)
for x in a:
    cnt[x] += 1
i, j = 0, n - 1
while cnt[a[i]] > 1:
    cnt[a[i]] -= 1
    i += 1
while cnt[a[j]] > 1:
    cnt[a[j]] -= 1
    j -= 1
print(i + 1, j + 1)
