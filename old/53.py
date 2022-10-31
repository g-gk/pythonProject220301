from sys import stdin
import string


def replace_whitespace(word):
    for w in string.whitespace:
        word = word.replace(w, ' ')
    return word


def smart_split(word):
    word = replace_whitespace(word)
    return [i for i in word.split(' ') if i]


matrix = []
for m in stdin:
    m = [int(i) for i in smart_split(m.split('\n')[0])]
    m.append(sum(m))
    matrix.append(m)
x = list(zip(*matrix))
sr = list(x[-1])  # список сумм строк
sc = [sum(i) for i in x[:-1]]  # список сумм столбцов
src = sr + sc  # список сумм строк и столбцов
res = all(x == src[0] for x in src[1:])
if res:
    print('YES')
else:
    print('NO')
