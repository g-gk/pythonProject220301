# Очередь с защитой от ошибок
st1, st2 = [], []
while True:
    com = input()
    if com == 'exit':
        print('bye')
        break
    elif 'push' in com:
        st1 += [com.split()[-1]]
        print('ok')
    elif com == 'pop':
        if st2:
            print(st2.pop())
        elif st1:
            while st1:
                st2 += [st1.pop()]
            print(st2.pop())
        else:
            print('error')
    elif com == 'front':
        if st2:
            print(st2[-1])
        elif st1:
            while st1:
                st2 += [st1.pop()]
            print(st2[-1])
        else:
            print('error')
    elif com == 'size':
        print(len(st1) + len(st2))
    elif com == 'clear':
        st1.clear()
        st2.clear()
        print('ok')
