# Составление расписания
nt = int(input())
t = set(map(int, input().split()))
nr = int(input())
r = set(map(int, input().split()))
nt1 = int(input())
t1 = set(map(int, input().split()))
nr1 = int(input())
r1 = set(map(int, input().split()))
ok = True
for el in t1:
    if el in t:
        ok = False
        print(-1)
        exit(0)
for el in sorted(r1):
    if el not in r:
        t |= t1
        r.add(el)
        print(len(t))
        print(*sorted(t))
        print(len(r))
        print(*sorted(r))
        exit(0)
print(-1)
