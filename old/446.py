# ребус на доске
cnt = 0
for sa1 in '2468':
    for sa2 in '02468':
        for sa3 in '13579':
            sa = sa1 + sa2 + sa3
            a = int(sa)
            for sb1 in '13579':
                b1 = int(sb1)
                for sb2 in '13579':
                    b2 = int(sb2)
                    sb = sb1 + sb2
                    b = int(sb)
                    c = a * b2
                    sc = str(c)
                    d = a * b1
                    sd = str(d)
                    e = a * b
                    se = str(e)
                    cnt += 1
                    # print(f'{a}*{b}={e}')
                    if (len(sc) == 4 and len(sd) == 3 and len(se) == 5 and
                            all(x in '02468' for x in sc[0] + sc[2] + sd[0]) and
                            all(x in '13579' for x in sc[1] + sc[-1] + sd[1:] + se)):
                        print('  ', a)
                        print(' x ', b)
                        print('------')
                        print(' ', c)
                        print('+', d)
                        print('------')
                        print('', e)
print(cnt)
