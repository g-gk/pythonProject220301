# Родословная
n = int(input())
tree = {}
for _ in range(n - 1):
    w = input().split()
    if w[1] in tree:
        tree[w[1]][w[0]] = {}
    else:
        if tree:
            for k in tree:
                if w[1] in tree[k]:
                    tree[k][w[1]] = {w[0]: {}}
        else:
            tree[w[1]] = {w[0]: {}}
print(tree)
