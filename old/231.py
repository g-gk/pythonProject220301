a = list(map(int, '100101010'))
print(a)


def t(a):
    return [[not a[0], a[1], a[2], a[3], a[4], not a[5], a[6], a[7], not a[8]],
            [a[0], not a[1], not a[2], a[3], a[4], a[5], a[6], not a[7], a[8]],
            [a[0], a[1], not a[2], a[3], a[4], not a[5], not a[6], a[7], not a[8]],
            [a[0], not a[1], not a[2], not a[3], a[4], a[5], a[6], a[7], a[8]],
            [not a[0], a[1], a[2], not a[3], not a[4], not a[5], a[6], a[7], a[8]],
            [a[0], not a[1], a[2], a[3], a[4], not a[5], not a[6], a[7], a[8]],
            [a[0], a[1], a[2], not a[3], not a[4], a[5], not a[6], not a[7], a[8]],
            [a[0], a[1], not a[2], a[3], a[4], a[5], a[6], not a[7], not a[8]],
            [not a[0], a[1], a[2], not a[3], a[4], a[5], a[6], a[7], not a[8]]]


b = t(a)
for i in range(9):
    s1 = ''.join(str(int(x)) for x in b[i])
    print(i + 1, s1)
    print('------------------')
    c = t(b[i])
    for j in range(9):
        s2 = ''.join(str(int(x)) for x in c[j])
        if s2 == '111111111':
            print(i + 1, j + 1, s2)
        d = t(c[j])
        for k in range(9):
            s3 = ''.join(str(int(x)) for x in d[k])
            if s3 == '111111111':
                print(i + 1, j + 1, k + 1, s3)
            e = t(d[k])
            for g in range(9):
                s4 = ''.join(str(int(x)) for x in e[g])
                if s4 == '111111111':
                    print(i + 1, j + 1, k + 1, g + 1, s4)
                f = t(e[g])
                for r in range(9):
                    s5 = ''.join(str(int(x)) for x in f[r])
                    if s5 == '111111111':
                        print(i + 1, j + 1, k + 1, g + 1, r + 1, s5)
