for a in '2468':
    for b in '02468':
        for c in '13579':
            for d in '13579':
                for e in '13579':
                    res = str(int(a + b + c) * int(d + e))
                    f = True
                    for i in res:
                        if i in '02468':
                            f = False
                    if len(res) == 5 and f:
                        x1 = str(int(e) * int(a + b + c))
                        x2 = str(int(d) * int(a + b + c))
                        if (len(x1) == 4 and len(x2) == 3 and x1[0] in '2468' and x2[0] in '2468' and
                                x1[2] in '02468' and x1[1] in '13579' and x1[-1] in '13579' and
                                x2[1] in '13579' and x2[-1] in '13579'):
                            print('  ' + a + b + c)
                            print(' x ' + d + e)
                            print('-----')
                            print(' ' + x1)
                            print('+' + x2)
                            print('-----')
                            print(res)
                            print()
