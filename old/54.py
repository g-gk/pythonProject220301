import itertools

carts = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
s = input()
suits.remove(s)
print('\n'.join([' '.join(i) for i in itertools.product(carts, suits)]))
