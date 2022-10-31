# Частотный анализ – 1
n = int(input())
text = ''
for _ in range(n):
    text += input() + ' '
text1 = ''
for c in text:
    if c.isalpha():
        text1 += c
    else:
        text1 += ' '
words = text1.split()
wd = {}
for w in words:
    lw = w.lower().capitalize()
    wd[lw] = wd.get(lw, 0) + 1
# print(wd)
print('\n'.join(w[0] for w in sorted(wd.items(), key=lambda x: (-x[1], x[0]))))
