# H1. Санчкин 1
n = int(input())
c, cnt = 0, 0
for i in range(n):
    w, sn = input().split()
    n = int(sn)
    if w == 'any':
        if n > 1:
            if c == 0 or n > 2:
                cnt += 2
                c += 2
            elif c == 1:
                cnt += 1
                c += 1
        else:
            cnt += n
            c += n
    else:
        cnt += n
    if c > 1:
        print(cnt)
        exit(0)
print('impossible')
