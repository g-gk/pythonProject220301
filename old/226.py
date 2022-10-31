# C. Улицы исправных фонарей
a1 = list(input())
print(a1)
n = len(a1)
a2 = [0] * n
stack = []
for i in range(n):
    if a1[i] == '(':
        stack.append(a1[i])
    elif a1[i] == '?':
        if stack:
            a2[i] = ')'
            stack.pop()
        else:
            a2[i] = '('
            stack.append('(')
    elif a1[i] == ')':
        if stack:
            stack.pop()
        else:
            print('Impossible')
            exit(0)

if stack:
    print('Impossible')
else:
    for i in range(n):
        if a1[i] == '?':
            a1[i] = a2[i]
    print(''.join(a1))
