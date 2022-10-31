# Именно та буква
line = input()
n = int(input())
letter = input()
if len(letter) > 1 or not letter.isalnum() or n < 0:
    print('ОШИБКА')
elif line.index(letter) + 1 == n:
    print('ДА')
else:
    print('НЕТ')