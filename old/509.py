# Минификатор
n = int(input())
for _ in range(n):
    line = input()
    new_line = []
    i = 0
    w = ''
    while line[i] == ' ':
        w += line[i]
        i += 1
    new_line += [w]
    k1 = -1
    w = ''
    while i < len(line):
        if line[i] == "'" and k1 < 0:
            new_line += [w]
            w = ''
            k1 = i
        elif line[i] == "'" and k1 >= 0 and (line[i - 1] != '\\' or line[i - 2:i] == '\\\\'):
            new_line += [line[k1:i + 1]]
            k1 = -1
        elif k1 < 0:
            if line[i] != '#':
                if line[i] != ' ' or line[i] == ' ' and line[i - 1] != ' ':
                    w += line[i]
            else:
                break
        i += 1
    new_line += [w]
    print(''.join(new_line))
