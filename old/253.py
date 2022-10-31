a = int(input())
b = int(input())
if a > 0 and b > 0 and (a % 2 == 0 or b % 2 == 0):
    print('ДА', end='')
else:
    print('НЕТ', end='')
