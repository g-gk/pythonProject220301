# Игра в пьяницу
# st1 = [int(x) if x != '0' else 10 for x in '1 3 5 7 0'.split()[::-1]]
# st2 = [int(x) if x != '0' else 10 for x in '2 4 6 8 9'.split()[::-1]]

st1 = [int(x) if x != '0' else 10 for x in input().split()[::-1]]
st2 = [int(x) if x != '0' else 10 for x in input().split()[::-1]]

st1t, st2t = [], []
for i in range(1_000_000):
    if not st1 and st1t:
        while st1t:
            st1 += [st1t.pop()]
    if not st2 and st2t:
        while st2t:
            st2 += [st2t.pop()]
    if not st1:
        print('second', i)
        exit(0)
    if not st2:
        print('first', i)
        exit(0)
    x, y = st1.pop(), st2.pop()
    if x > y:
        st1t += [x, y]
    else:
        st2t += [x, y]
    # print(f'--------{i}----------')
    # print(st1, st1t)
    # print(st2, st2t)
print('botva')
