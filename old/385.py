# Диофантово уравнение
def gcd_ext(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd_ext(b, a % b)
    x, y = y, x - (a // b) * y
    return d, x, y


a, b, c = map(int, input().split())
d, x, y = gcd_ext(a, b)
if c % d:
    print(-1)
else:
    x, y = c // d * x, c // d * y
    t = x // (b // d)
    print(x - b // d * t, y + a // d * t)
