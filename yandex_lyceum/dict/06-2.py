# Права доступа
n = int(input())
s1 = set()
for _ in range(n):
    s1.add(input().strip())
m = int(input())
for _ in range(m):
    cur = input().strip().split('/')
    p = ''
    ok = False
    for x in cur:
        if x:
            p += '/' + x
        if p in s1:
            print('YES')
            ok = True
            break
    if not ok:
        print('NO')
