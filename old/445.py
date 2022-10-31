# ребус на доске
x = [0, 2, 4, 6, 8]
y = [1, 3, 5, 7, 9]
for a in range(100, 1000):
    a1, a2, a3 = a // 100, a // 10 % 10, a % 10
    if a1 in x and a2 in x and a3 in y:
        for b in range(10, 100):
            b1, b2 = b // 10, b % 10
            if b1 in y and b2 in y:
                c = a * b2
                sc = str(c)
                d = a * b1
                sd = str(d)
                e = a * b
                se = str(e)
                if (len(sc) == 4 and len(sd) == 3 and len(se) == 5 and
                        sc[0] in '02468' and sc[2] in '02468' and
                        sc[1] in '13579' and sc[3] in '13579' and
                        sd[0] in '02468' and sd[1] in '13579' and sd[2] in '13579' and
                        all(t in '13579' for t in se)):
                    print('  ', a)
                    print(' x ', b)
                    print('------')
                    print(' ', c)
                    print('+', d)
                    print('------')
                    print('', e)
