# Крупные буквы
s = input()
let_a = [' * ', '* *', '***', '* *', '* *']
let_b = ['** ', '* *', '** ', '* *', '** ']
let_c = [' * ', '* *', '*  ', '* *', ' * ']
ans = [[] for _ in range(5)]
for c in s:
    for i in range(5):
        if c == 'A':
            ans[i] += [let_a[i]]
        elif c == 'B':
            ans[i] += [let_b[i]]
        elif c == 'C':
            ans[i] += [let_c[i]]
for i in range(5):
    print('  '.join(ans[i]))
