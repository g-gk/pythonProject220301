from sys import stdin
import string


def del_punct(word):
    while word[-1] in string.punctuation:
        word = word[:-1]
    return word


word = []
res = []
for s in stdin:
    s = s.split('\n')[0].split(' ')
    print(s)
s = [del_punct(i) for i in s if i]
word += s
word = enumerate(word)
print(*word)
for i, w in word:
    if w == w.capitalize() and w not in [e[0] for e in res]:
        res.append((w, i))
res.sort()
for a in res:
    print(f'{a[-1]} - {a[0]}')
