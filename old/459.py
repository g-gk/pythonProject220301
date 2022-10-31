# Контрольная по ударениям
n = int(input())
wd = {}
for _ in range(n):
    w = input()
    wd[w.lower()] = wd.get(w.lower(), []) + [w]
words = input().split()
count = 0
for w in words:
    cnt = 0
    for c in w:
        if c.isupper():
            cnt += 1
    lw = w.lower()
    if cnt != 1 or cnt == 1 and lw in wd and w not in wd[lw]:
        count += 1
print(count)
