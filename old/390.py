n = int(input())
divs = []
step = []
d = 2
while d ** 2 <= n:
    c = 0
    while n % d == 0:
        n //= d
        c += 1
    if c:
        divs += [d]
        step += [c]
    d += 1
if n > 1:
    divs += [n]
    step += [1]
print(divs)
print(step)
