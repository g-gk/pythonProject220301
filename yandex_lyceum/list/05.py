# RLE
s = input() + '*'
c = s[0]
cnt = 1
ans = []
for x in s[1:]:
    if x == c:
        cnt += 1
    else:
        ans += [str(cnt) + ' ' + c]
        c = x
        cnt = 1
print('\n'.join(ans))
