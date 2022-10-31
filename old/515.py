# Ползём вниз
com = input()
c = com[0]
line = [c]
i = 1
for x in com[1:]:
    if x == 'V':
        print(''.join(line))
        line = [' '] * (i - 1) + [c]
    elif x == '>':
        line += [c]
        i += 1
    elif x == '<':
        i -= 1
        line[i - 1] = c
if line:
    print(''.join(line))
