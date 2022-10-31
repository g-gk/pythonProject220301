# Кто последний?
q = []
n = int(input())
for _ in range(n):
    w = input()
    if 'последний' in w:
        q.append(w.split('-')[-1][1:-1])
    elif 'спросить' in w:
        q.insert(0, w.split('-')[-1][1:-1])
    elif w == 'Следующий!':
        if q:
            print(f'Заходит {q.pop(0)}!')
        else:
            print('В очереди никого нет.')
