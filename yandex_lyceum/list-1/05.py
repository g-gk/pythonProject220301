# Пристраиваемся в очередь
n = int(input())
q = []
for _ in range(n):
    s = input()
    if 'встал' in s:
        name = s.split(' встал')[0]
        q.append(name)
    elif 'будет' in s:
        name1 = s.split('! ')[0].split('Привет, ')[1]
        name2 = s.split('! ')[1].split(' будет')[0]
        q.insert(q.index(name1) + 1, name2)
    elif 'хватит' in s:
        name = s.split(', хватит')[0]
        q.remove(name)
print('\n'.join(q))
