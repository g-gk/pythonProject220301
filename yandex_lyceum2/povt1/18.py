# Продавец мороженого
n = int(input())
d = {}
for _ in range(n):
    words = input().split()
    name, cost = ''.join(words[:-1]), int(words[-1])
    d[name] = cost
total, cur = 0, 0
line = input()
count = 1
while line != '.':
    line = input()
    if line and line != '.':
        words = line.split()
        name, cnt = ''.join(words[:-1]), int(words[-1])
        cur += cnt * d[name]
    elif not line or line == '.':
        if cur:
            print(f'{count}) {cur}')
            total += cur
            count += 1
            cur = 0
print(f'Итого: {total}')
