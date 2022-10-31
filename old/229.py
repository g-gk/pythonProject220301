n = int(input())
s = 'ABCDEF'
if n < 3:
    print(f'1{s[n + 3]}')
elif n > 118:
    print('full')
elif n > 116:
    print(f'21{s[n - 114]}')
else:
    print(f'{(n - 3) // 6 + 2}{s[(n - 3) % 6]}')
