from anytree import Node, RenderTree
from sys import stdin

data = stdin
kod = ''
klasses = []
for i in data:
    s = i.split(':')[0].split()
    if s and s[0] == 'class':
        if s[1].count('(') == 1 and s[1].count(')') == 1:
            klassproi = s[-1].split('(')[0].split(')')[0]
            klassbase = s[-1].split('(')[1].split(')')[0]
            kod += f'{klassproi} = Node("{klassproi}", parent={klassbase})\n'
        else:
            kod += f'{s[1]} = Node("{s[1]}")\n'
            klasses += [s[1]]
exec(kod)
for i in klasses:
    for pre, fill, node in RenderTree(eval(i)):
        print("%s%s" % (pre, node.name))