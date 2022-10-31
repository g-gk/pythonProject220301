# Сортировка вагонов
st, w2 = [], []
n = int(input())
w1 = list(map(int, input().split()))
cur = 1
ans = []
i = 0
while i < n:
    k = 0
    while i + k < n and w1[i + k] != cur:
        st += [w1[i + k]]
        k += 1
    i += k + 1
    if i <= n:
        st += [w1[i - 1]]
    ans += [f'1 {k + 1}']
    j = 0
    while st and st[-1] == cur:
        w2 += [st.pop()]
        cur += 1
        j += 1
    ans += [f'2 {j}']
if len(w2) == n:
    print('\n'.join(ans))
else:
    print(0)
