import itertools

suits = ['пик', 'треф', 'бубен', 'червей']
suit = input()
del suits[suits.index(suit)]
nom = [*range(2, 11), 'валет', 'дама', 'король', 'туз']
result = itertools.product(nom, suits)
for i in result:
    print(*i)
