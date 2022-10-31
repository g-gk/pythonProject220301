# Стек с защитой от ошибок
st = []
while True:
    com = input()
    if com == 'size':
        print(len(st))
    elif com == 'clear':
        st.clear()
        print('ok')
    elif com == 'exit':
        print('bye')
        break
    elif com == 'back':
        if st:
            print(st[-1])
        else:
            print('error')
    elif com == 'pop':
        if st:
            print(st.pop())
        else:
            print('error')
    elif 'push' in com:
        st.append(com.split()[-1])
        print('ok')
