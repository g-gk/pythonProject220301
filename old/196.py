def vinipuch(string):
    s = sum(1 for i in string if i in 'аеёиоуыэюя')
    return s


s1 = input().lower().split()
t = vinipuch(s1[0])
if all([vinipuch(i) == t for i in s1]):
    print('Парам пам-пам')
else:
    print('Пам парам')
