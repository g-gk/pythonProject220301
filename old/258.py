word = input()
x = int(input())
p = ''
ans = ''
for c in word:
    # print(p + c)
    ans += p + c + '\n'
    p += ' '
    if len(p) == x:
        p = ''
print(ans[:-1], end='')
