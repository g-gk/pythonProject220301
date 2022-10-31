# Игра в пьяницу
# st11 = [int(x) for x in '1 3 5 7 9'.split()]
# st21 = [int(x) for x in '2 4 6 8 0'.split()]
st11 = [int(x) for x in input().split()]
st21 = [int(x) for x in input().split()]

st12, st22 = [], []
for i in range(1_000_000):
    if not st12 and st11:
        st12 = st11[::-1]
        st11.clear()
    if not st22 and st21:
        st22 = st21[::-1]
        st21.clear()
    if not st12:
        print('second', i)
        exit(0)
    if not st22:
        print('first', i)
        exit(0)
    x, y = st12.pop(), st22.pop()
    if (x, y) == (0, 9) or (x, y) != (9, 0) and x > y:
        st11 += [x, y]
    elif (x, y) == (9, 0) or (x, y) != (0, 9) and x < y:
        st21 += [x, y]
    # print(f'--------{i}----------')
    # print(st11, st12)
    # print(st21, st22)
print('botva')
