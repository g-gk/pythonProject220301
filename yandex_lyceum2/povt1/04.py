# Репка
names = input().split(' -> ')
n = int(input())
for _ in range(n):
    name = input()
    idx = names.index(name)
    if idx == 0:
        print(f'{name} -> {names[1]}')
    elif idx == len(names) - 1:
        print(f'{names[-2]} -> {name}')
    else:
        print(f'{names[idx - 1]} -> {name} -> {names[idx + 1]}')
