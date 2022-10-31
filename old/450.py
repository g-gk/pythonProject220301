# Дек с защитой от ошибок
from collections import deque

d = deque()
while True:
    com = input()
    if 'push_front' in com:
        d.appendleft(com.split()[-1])
        print('ok')
    elif 'push_back' in com:
        d.append(com.split()[-1])
        print('ok')
    elif 'pop_front' in com:
        if d:
            print(d.popleft())
        else:
            print('error')
    elif 'pop_back' in com:
        if d:
            print(d.pop())
        else:
            print('error')
    elif com == 'front':
        if d:
            print(d[0])
        else:
            print('error')
    elif com == 'back':
        if d:
            print(d[-1])
        else:
            print('error')
    elif com == 'size':
        print(len(d))
    elif com == 'clear':
        d.clear()
        print('ok')
    elif com == 'exit':
        print('bye')
        break
