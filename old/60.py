import itertools
carts = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
all_var = [list(i) for i in itertools.product(carts, suits)]
all_combination = [', '.join([' '.join(i) for i in sorted(combination)])
                   for combination in itertools.permutations(all_var, 3)
                   if (suits[3] in [i[1] for i in combination])
                   and len([len(i[0]) for i in combination if len(i[0]) > 2]) > 0]

all_combination = set(all_combination)
all_combination = list(all_combination)
all_combination.sort()
print('\n'.join(all_combination))
