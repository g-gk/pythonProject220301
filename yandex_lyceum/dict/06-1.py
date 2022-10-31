# Права доступа
n = int(input())
d1 = []
for _ in range(n):
    d1.append(''.join(input().strip().split('/')))
m = int(input())
for _ in range(m):
    cur = ''.join(input().strip().split('/'))
    ok = False
    for el in d1:
        if el and cur.startswith(el):
            print('YES')
            ok = True
            break
    if not ok:
        print('NO')
