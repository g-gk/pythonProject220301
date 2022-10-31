# Ёлочка
def makeLevel(i):
    for j in range(i + 1):
        print('*' * (j + 1))


def tree(n):
    for i in range(n):
        makeLevel(i + 1)


n = int(input())
tree(n)
