# Степень
a = a1 = int(input())
divs = []
step = []
d = 2
while d ** 2 <= a:
    c = 0
    while a % d == 0:
        a //= d
        c += 1
    if c > 0:
        divs += [d]
        step += [c]
    d += 1
if a > 1:
    divs += [a]
    step += [1]
ans = 1
for el in divs:
    ans *= el
if ans >= 30:
    print(ans)
else:
    for k in range(1, 30):
        n = k * ans
        f = 1
        for i in range(1, n + 1):
            f = n * f % a1
        if f == 0:
            print(n)
            break
