n = int(input())
w = 'получил'
ans = []
for i in range(n):
    s = input().split()
    if s[0] in ('Соня', 'Маша'):
        # print(' '.join(s[:2] + [w + 'а'] + s[2:]), end='.\n')
        ans.append(' '.join(s[:2] + [w + 'а'] + s[2:]) + '.')
    else:
        # print(' '.join(s[:2] + [w] + s[2:]), end='.\n')
        ans.append(' '.join(s[:2] + [w] + s[2:]) + '.')
print(*ans, sep='\n', end='')
