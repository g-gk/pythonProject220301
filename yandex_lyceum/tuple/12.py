# Наборщик
en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
s = input()
ans = []
for c in set(s):
    f = False
    for i in range(len(en)):
        if c == en[i]:
            ans += [(c, i + 1)]
            f = True
            break
    if f:
        continue
    for i in range(len(ru)):
        if c == ru[i]:
            ans += [(c, i + 1)]
            break
print(*ans, sep='\n')
