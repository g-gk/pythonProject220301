# Числовые функции
x = int(input())
if x == 1:
    print(1, 1)
    exit(0)
s0, s1 = 1, 1
sqrtx = int(x ** 0.5)
for d in range(2, sqrtx + 1):
    if x % d == 0:
        s0 += 2
        s1 += d + x // d
s0 += 1
s1 += x
if sqrtx ** 2 == x:
    s0 -= 1
    s1 -= sqrtx
print(s0, s1)
