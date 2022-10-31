# Камень, ножницы, бумага
line1 = input()
line2 = input()
if line1 == line2:
    print('ничья')
elif line1 == 'камень':
    if line2 == 'ножницы':
        print('первый')
    elif line2 == 'бумага':
        print('второй')
elif line1 == 'ножницы':
    if line2 == 'камень':
        print('второй')
    elif line2 == 'бумага':
        print('первый')
elif line1 == 'бумага':
    if line2 == 'камень':
        print('первый')
    elif line2 == 'ножницы':
        print('второй')
