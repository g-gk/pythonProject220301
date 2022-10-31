# C. Проверка правописания
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n != 5:
        print('no')
    elif sorted(s) != sorted('Timur'):
        print('no')
    else:
        print('yes')
