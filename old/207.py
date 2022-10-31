from itertools import product

d = input()

suits = ['пик', 'треф', 'бубен', 'червей']
items = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')

suits.remove(d)

for n, s in product(items, suits):
    print(n, s)
