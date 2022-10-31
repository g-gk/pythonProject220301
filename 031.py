from math import factorial


def is_palindrome(n):
    sn = str(n)
    return sn == sn[::-1]


mx = 0
ans = []
f9 = factorial(10)
for ki in range(f9, f9 + 1):
    si = '1' * ki
    i = int(si)
    cnt = 0
    for kj in range(1, 1000):
        sj = '1' * kj
        j = int(sj)
        if i % j == 0:
            ij = i // j
            if sj == sj[::-1] and is_palindrome(ij):
                cnt += 1
                # print(i, cnt, j, i // j)
                # ans.append(f'{i} {cnt} {j} {ij}')
    mx = max(mx, cnt)
# with open('res.txt', 'w') as f:
#     f.write('\n'.join(ans))
print(mx)
