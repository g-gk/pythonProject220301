s = input()
for c in s:
    if c not in '01234567':
        print('NO')
        exit(0)
n = int(s, 8)
if n % 7 == 0:
    print('YES')
else:
    print('NO')
