# Родословная
from sys import stdin

data = list(map(str.strip, stdin))
# n = int(input())
n = int(data[0])
s0, s1 = set(), set()
for x in data[1:]:
    a, b = x.split()
    s0.add(a)
    s1.add(b)
w0 = list(s1 - s0)[0]
tree = {w0: 0}
for x in data[1:]:
    # w = input().split()
    w = x.split()
    if w[1] in tree:
        tree[w[0]] = tree[w[1]] + 1
    else:
        if w[0] in tree:
            tree[w[1]] = tree[w[0]] - 1
        else:
            tree[w[0]] = 1
            tree[w[1]] = 0
    # print(tree)
for x in sorted(tree.keys()):
    print(x, tree[x])
# print(tree)
