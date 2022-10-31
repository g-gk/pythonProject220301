from math import factorial

n = factorial(2022)
sn = str(n)
print(len(sn))
cnt0 = 0
i = -1
while sn[i] == '0':
    cnt0 += 1
    i -= 1
print(cnt0)
for x in range(2, 500):
    x2 = 2 ** x
    for y in range(2, 500):
        y3 = 3 ** y
        for z in range(2, 500):
            z5 = 5 ** z
            res = x2 + y3 + z5
            sr = str(res)
            if '0' * 7 in sr[-7:]:
                print(x, y, z, x2, y3, z5, res)
                # print(n - res)
                print(len(sr))
