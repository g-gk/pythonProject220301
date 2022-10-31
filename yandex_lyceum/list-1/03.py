# Парадоксы статистики
def stat(a: list):
    a.sort()
    n = len(a)
    if n % 2:
        med = a[n // 2]
    else:
        med = (a[n // 2 - 1] + a[n // 2]) / 2
    moda = a[0]
    mx = 1
    for x in set(a):
        cntx = a.count(x)
        if cntx > mx:
            moda = x
            mx = cntx
    return med, moda


n = int(input())
total = []
medians = []
mods = []
for _ in range(n):
    a = list(map(int, input().split()))
    res = stat(a)
    total += a
    medians.append(res[0])
    mods.append(res[1])
print(*medians)
print(*mods)
print(stat(medians)[0])
print(stat(mods)[1])
print(*stat(total), sep='\n')
