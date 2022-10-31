# Удалить повторы
s = input()
ss = set()
res = ''
for c in s:
    if c not in ss:
        res += c
        ss.add(c)
print(res)
