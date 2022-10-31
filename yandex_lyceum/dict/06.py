# Права доступа
n = int(input())
d1 = []
for _ in range(n):
    d1.append(input().strip())
m = int(input())
for _ in range(m):
    cur = input().strip()
    ok = False
    for el in d1:
        if cur.startswith(el):
            print('YES')
            ok = True
            break
    if not ok:
        print('NO')
