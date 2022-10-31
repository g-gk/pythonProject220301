# Постфиксная запись
st = []
s = input().split()
for c in s:
    if c == '+':
        st += [st.pop() + st.pop()]
    elif c == '-':
        st += [-st.pop() + st.pop()]
    elif c == '*':
        st += [st.pop() * st.pop()]
    else:
        st += [int(c)]
print(st[0])
