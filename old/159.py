# Энты

def f(a, k):
    for el in a:
        if el <= k:
            return True
    return False


k, p = map(int, input().split())
e = [2]
ans = 0
while f(e, k):
    t = []
    for el in e:
        x, y = el + 1, 2 * el
        for q in (x, y):
            if q == k:
                ans += 1
        t += [x, y]
    e = t
print(ans % p)
