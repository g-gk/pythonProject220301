# Разложение на простые
n = int(input())
p = {}
d = 2
while d ** 2 <= n:
    if n % d == 0:
        if d in p:
            p[d] += 1
        else:
            p[d] = 1
        n //= d
    else:
        d += 1
if n > 1:
    if n in p:
        p[n] += 1
    else:
        p[n] = 1
ans = [f'{k}^{v}' if v > 1 else str(k) for k, v in p.items()]
print(*ans, sep='*')
