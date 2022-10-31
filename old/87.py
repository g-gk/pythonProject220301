s = input()
res = ''
flag = True
for c in s:
    if flag or c == '}':
        res += c
    if c == '{':
        flag = False
    if c == '}':
        flag = True
print(res)
