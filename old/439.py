# Правильная скобочная последовательность
st = []
s = input()
ok = True
for c in s:
    if c in '([{':
        st += [c]
    elif c == ')':
        if st and st[-1] == '(':
            st.pop()
        else:
            ok = False
            break
    elif c == ']':
        if st and st[-1] == '[':
            st.pop()
        else:
            ok = False
            break
    elif c == '}':
        if st and st[-1] == '{':
            st.pop()
        else:
            ok = False
            break
if not ok or st:
    print('no')
else:
    print('yes')
