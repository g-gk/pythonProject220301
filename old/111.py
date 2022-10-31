# G. Водная битва
n = int(input())
ab = [0] * 8
cnt = [0, 0]
for i in range(n):
    t, a, b = map(int, input().split())
    if a in (1, 2, 3, 4):
        cnt[0] += 100
        if t - ab[a - 1] <= 10 and ab[a - 1] != 0:
            cnt[0] += 50
    elif a in (5, 6, 7, 8):
        cnt[1] += 100
        if t - ab[a - 1] <= 10 and ab[a - 1] != 0:
            cnt[1] += 50
    ab[a - 1] = t
print(*cnt)
