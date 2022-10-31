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
    t = 0
    if x < 0:
        while x < 0:
            t += 1
            x += b // d
    elif x > 0:
        while x >= 0:
            t -= 1
            x -= b // d
        t += 1
        x += b // d
    y = y - a // d * t
    print(x, y)
