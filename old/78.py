# voda*5=more
for voda in range(1000, 10000):
    more = voda * 5
    sm = str(more)
    sv = str(voda)
    if (len(sm) == 4 and sm[1] == sv[1] and
            len(set(sm + sv)) == 7):
        print(f'{voda} * 5 = {more}')
