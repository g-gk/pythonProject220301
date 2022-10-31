import sys

marks = '!()-[]{};?@#$%\':\",./^&*_\\'
text = ' '.join(list(map(str.strip, sys.stdin)))
text = ''.join([x for x in text if x not in marks])
spisok = []
spisok2 = filter(lambda y: y[1] == y[1].capitalize(), enumerate(text.split()))
spisok3 = []
for i in spisok2:
    if i[1] not in spisok:
        spisok3.append(i)
        spisok.append(i[1])
spisok3 = sorted(spisok3, key=lambda x: x[1])
for i in spisok3:
    print(*i, sep=' - ')
