# Нолики-крестики
n = int(input())
a = [input() for _ in range(n)]
for c in 'xo':
    for r in a + [''.join(x) for x in zip(*a)]:
        if c * 3 in r:
            print(c)
            exit(0)
print('-')
