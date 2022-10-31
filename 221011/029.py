m, s, p, q = [int(input()) for _ in range(4)]
# print(m, s, p, q)
time = (48 - m) * 60 - s
f1 = True
f2 = False
f3 = True
while time > 23:
    if f1:
        p += 3
        f1 = False
        f2 = True
    elif f2:
        q += 2 * f3
        f3 = not f3
        f2 = False
        f1 = True
    time -= 24
print(p)
print(q)
