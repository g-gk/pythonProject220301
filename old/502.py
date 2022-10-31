# Рецепты
m = int(input())
prod = set(input() for _ in range(m))
n = int(input())
ans = []
for i in range(n):
    name = input()
    k = int(input())
    ok = True
    for i in range(k):
        if input() not in prod:
            ok = False
    if ok:
        ans += [name]
print('\n'.join(ans))
