# Джек-Победитель-Великанов
n = int(input())
a = []
for i in range(n):
    line = input()
    b = []
    while line != '*':
        b += line.split()
        line = input()
    a += ['-'.join(b)]
print(', '.join(a[::-1]))
