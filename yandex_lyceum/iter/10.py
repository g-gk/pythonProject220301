# Карточные расклады
from itertools import combinations, product

mast = ['червей', 'бубен', 'пик', 'треф']
rank = list(range(2, 11)) + 'валет-дама-король-туз'.split('-')
rank = list(map(str, rank))
karts = (x[0] + ' ' + x[1] for x in product(rank, mast))
ans = []
for x in combinations(karts, 3):
    ok = False
    y = ' '.join(x)
    if 'червей' in y:
        for el in rank[-4:]:
            if el in y:
                ok = True
                break
        if ok:
            ans.append(', '.join(sorted(x)))
print('\n'.join(sorted(ans)))
