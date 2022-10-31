# Вертикальная диаграмма
a = list(map(int, input().split()))
n, mx = len(a), max(a)
print('*' * (n + 2))
print('*' + ' ' * n + '*')
x = mx
while x > 0:
    t = '*'
    for y in a:
        if y >= x:
            t += '*'
        else:
            t += ' '
    print(t + '*')
    x -= 1
