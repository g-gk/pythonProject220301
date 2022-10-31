# Разные разности
n = int(input())
sa = {int(input()) for _ in range(n)}
ans = set()
for x in sa:
    for y in sa:
        ans.add(x - y)
print(*sorted(ans), sep='\n')
