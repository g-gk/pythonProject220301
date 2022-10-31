# Точки на плоскости
n = int(input())
ans = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
for _ in range(n):
    xy = input().split()
    if '0' in xy:
        print(f'({xy[0]}, {xy[1]})')
    else:
        if '-' in xy[0] and '-' in xy[1]:
            ans['III'] += 1
        elif '-' in xy[0]:
            ans['II'] += 1
        elif '-' in xy[1]:
            ans['IV'] += 1
        else:
            ans['I'] += 1
print(', '.join(f'{k}: {v}' for k, v in ans.items()), end='.')
