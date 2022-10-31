# Обработка текста
from sys import stdin

data = stdin.read()
text = ''
for i in range(len(data)):
    if data[i].isalpha() or data[i] in "'-":
        text += data[i]
    else:
        text += ' '
words = text.split()
# print(words)
set_words = set()
ans = []
for el in enumerate(words):
    if el[1] not in set_words:
        ans.append(el)
        set_words.add(el[1])
ans = filter(lambda x: x[1][0] == x[1][0].upper(), ans)
for x in sorted(ans, key=lambda x: x[1]):
    print(f'{x[0]} - {x[1]}')
