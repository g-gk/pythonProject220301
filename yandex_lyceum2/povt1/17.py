# Корпоративная почта
n = int(input())
domen = 'untitled.py'
names = {}
for _ in range(n):
    t = input().split('@')[0]
    if t[-1].isdigit():
        for i in range(len(t) - 1, 0, -1):
            if t[i].isdigit():
                name = t[:i]
                k = int(t[i:])
                names[name] = k
                break
    else:
        names[t] = 0
m = int(input())
for _ in range(m):
    name = input()
    if name in names:
        names[name] += 1
        print(f'{name}{names[name]}@{domen}')
    else:
        print(f'{name}@{domen}')
        names[name] = 0
