city1 = input().strip().lower()
city2 = input().strip().lower()
if city1 == 'вена' and city2 == 'прага':
    print('НЕТ')
elif city1 != city2 and (city1 == 'вена' or city2 == 'прага'):
    print('ДА')
else:
    print('НЕТ')
