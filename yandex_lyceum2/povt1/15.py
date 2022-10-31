# Вопросительное повествование без восклицаний
from sys import stdin

text = ' '.join(line.rstrip() for line in stdin.readlines()).lower()
predl = ''
set1, set2, set3 = set(), set(), set()
for c in text:
    if c in '.?!':
        if c == '.':
            set1 |= set(predl.split())
        elif c == '?':
            set2 |= set(predl.split())
        elif c == '!':
            set3 |= set(predl.split())
        predl = ''
    else:
        predl += c
print(*sorted(set1 & set2 - set3))
