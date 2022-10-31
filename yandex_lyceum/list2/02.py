# bf
ceils = [0] * 30000
commands = input()
n = len(commands)
a = []
b = []
stack = []
for i in range(n):
    if commands[i] == '[':
        stack.append(i)
    elif commands[i] == ']':
        a.append(stack.pop())
        b.append(i)
i = 0
j = 0
while j < n:
    com = commands[j]
    if com == '>':
        i += 1
        i %= 30000
    elif com == '<':
        i -= 1
        i %= 30000
    elif com == '+':
        ceils[i] += 1
        ceils[i] %= 256
    elif com == '-':
        ceils[i] -= 1
        ceils[i] %= 256
    elif com == '.':
        print(ceils[i])
    elif com == '[':
        if ceils[i] == 0:
            j = b[a.index(j)]
    elif com == ']':
        j = a[b.index(j)] - 1
    j += 1
