# Очередь с поддержкой минимума
n = int(input())
st1, st2, stm, mn = [], [], [], 100000
for i in range(n):
    a = int(input())
    if a > 0:
        st1 += [a]
        mn = min(mn, a)
    elif a == 0:
        if st2:
            x = stm[-1]
            if x <= mn:
                print(stm.pop())
            else:
                print(mn)
                stm.pop()
            st2.pop()
        elif st1:
            while st1:
                x = st1.pop()
                st2 += [x]
                if stm:
                    stm += [min(x, stm[-1])]
                else:
                    stm += [x]
            mn = 100000
            print(stm.pop())
            st2.pop()
        else:
            print(-1)
            mn = 100000
    # print(n, a, st1, st2, stm, mn)
