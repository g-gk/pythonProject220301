t = set(range(1, 101))

while True:
    delt = set()
    for a in t:
        ok = True
        for b in t - {a}:
            if b > (a / 2) ** 2:
                delt.add(a)
                ok = False
                break
        if not ok:
            break
    if not ok:
        t -= {a}
    if not delt:
        break
print(sorted(t))
print(len(t))
# 81
