# Камень, ножницы, бумага, ром, пират
line1 = input()
line2 = input()
if line1 == line2:
    print('ничья')
elif line1 == 'камень':
    if line2 in ('ром', 'ножницы'):
        print('первый')
    elif line2 in ('бумага', 'пират'):
        print('второй')
elif line1 == 'ножницы':
    if line2 in ('камень', 'пират'):
        print('второй')
    elif line2 in ('ром', 'бумага'):
        print('первый')
elif line1 in 'бумага':
    if line2 in ('камень', 'пират'):
        print('первый')
    elif line2 in ('ножницы', 'ром'):
        print('второй')
elif line1 in 'ром':
    if line2 in ('бумага', 'пират'):
        print('первый')
    elif line2 in ('камень', 'ножницы'):
        print('второй')
elif line1 in 'пират':
    if line2 in ('ножницы', 'камень'):
        print('первый')
    elif line2 in ('ром', 'бумага'):
        print('второй')
