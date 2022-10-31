p = int(input())
cnt = 0
for x in range(1, p):
    if (x ** (p - 1) - 1) % p == 0:
        flag = True
        t = x
        for y in range(1, p - 1):
            if (t - 1) % p == 0:
                flag = False
                break
            t *= x
        # t *= x
        # print(x, t, flag)
        if flag:
            cnt += 1
print(cnt)
