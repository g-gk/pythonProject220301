from itertools import product

for i in range(1, 30):
    print(i)
    for s1 in product(('1', '2', '21', '22222222'), repeat=i):
        s = '0' + ''.join(s1) + '0'
        # print(s)
        while '00' not in s:
            s = s.replace('021', '102', 1)
            s = s.replace('022', '301', 1)
            s = s.replace('02', '20', 1)
            s = s.replace('01', '10', 1)

        cnt1 = s.count('1')
        cnt2 = s.count('2')
        cnt3 = s.count('3')
        if cnt1 == 27 and cnt3 == 4:
            print(s)
            print(cnt1, cnt2, cnt3)
