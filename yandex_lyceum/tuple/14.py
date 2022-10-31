# Колобок и кочки
n = int(input())
cnt = [int(input()) for _ in range(n)]
ans = ''
for i in range(n):
    w = input()
    cur = ''
    for c in set(w):
        if w.count(c) == cnt[i]:
            if cur:
                print('нечленораздельно')
                exit(0)
            else:
                cur = c
    if cur:
        ans += cur
    else:
        print('нечленораздельно')
        exit(0)

print(ans)
