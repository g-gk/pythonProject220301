# Суперчисла
a, b = map(int, input().split())
pb = [i for i in range(0, b + 1)]
pb[:2] = [0, 0]
for i in range(2, b + 1):
    if pb[i]:
        for j in range(i ** 2, b + 1, i):
            pb[j] = 0
p = [i for i in pb if i > 0]
# print(p)
ans = set()
for i in range(len(p)):
    for j in range(i, len(p)):
        s = p[i] + p[j]
        if a <= s <= b:
            ans.add(s)
print(*sorted(list(ans)), sep='\n')
