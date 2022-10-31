# H1. Санчкин 1
n = int(input())
r, l, cnt_any = 0, 0, 0
for i in range(n):
    w, sk = input().split()
    k = int(sk)
    if w == 'right':
        r += k
    elif w == 'left':
        l += k
    elif w == 'any':
        cnt_any += k
if (r == 0 and cnt_any == 0 or l == 0 and cnt_any == 0 or
        l == 0 and r == 0 and cnt_any < 2):
    print('impossible')
elif l > 0 or r > 0:
    print(max(r, l) + 1)
else:
    print(2)
