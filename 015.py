a = 'X'
b = 'У'
s = a
for _ in range(4):
    for c in s:
        if c == a:
            s += b
        else:
            s += a
    print(s)
