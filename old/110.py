# H2. Санчкин 2
n = int(input())
r, l, cnt_any = 0, 0, 0
d = {}
for i in range(n):
    key, w, sk = input().split()
    k = int(sk)
    if key in d:
        if w == 'right':
            d[key][0] += k
        elif w == 'left':
            d[key][1] += k
        elif w == 'any':
            d[key][2] += k
    else:
        d[key] = [0, 0, 0]
        if w == 'right':
            d[key][0] = k
        elif w == 'left':
            d[key][1] = k
        elif w == 'any':
            d[key][2] = k
# print(d)
mx = 0
f = False
for k, v in d.items():
    if not (v[0] == 0 and v[2] == 0 or v[1] == 0 and v[2] == 0 or
            v[0] == 0 and v[1] == 0 and v[2] < 2):
        f = True
    #     print('impossible')
    # elif l > 0 or r > 0:
    #     print(max(r, l) + 1)
    # else:
    #     print(2)
    # if v[0] > 0 and (v[1] + v[2] > 0) or v[1] > 0 and (v[0] + v[2] > 0):
    mx += max(v[0], v[1], 1 if v[2] > 0 else 0)
if mx != 0:
    print(mx + 1)
elif f:
    print(2)
else:
    print('impossible')
