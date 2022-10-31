# Колода карт
from itertools import product

a = ['пик', 'треф', 'бубен', 'червей']
b = list(range(2, 11)) + 'валет дама король туз'.split()
a.remove(input())
for x in product(b, a):
    print(*x)
