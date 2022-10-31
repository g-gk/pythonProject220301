def f(s):
    t = 0
    for c in s:
        if c == '+':
            if t < 30:
                t += 1
            elif 30 <= t <= 59:
                t += 5
            elif 60 <= t < 2 * 60:
                t += 10
            elif t >= 2 * 60:
                t += 60
        elif c == '-':
            if 0 < t < 30:
                t -= 1
            elif 30 <= t <= 59:
                t -= 5
            elif 60 <= t < 2 * 60:
                t -= 10
            elif t >= 2 * 60:
                t -= 60
        elif c == '#':
            t += 30
    return t // 60, t % 60


s = '#+#-'
m, sec = f(s)
print(f'test [{s}] - {m}\' {sec}"')

s = '++#+'
m, sec = f(s)
print(f'1 [{s}] - {m}\' {sec}"')

s = '####+'
m, sec = f(s)
print(f'2 [{s}] - {m}\' {sec}"')

s = '++#+#+##+'
m, sec = f(s)
print(f'3 [{s}] - {m}\' {sec}"')

s = '#--#+#++#+'
m, sec = f(s)
print(f'4 [{s}] - {m}\' {sec}"')

s = '#-++#####+'
m, sec = f(s)
print(f'5 [{s}] - {m}\' {sec}"')

s = '#-++#####++'
m, sec = f(s)
print(f'6 [{s}] - {m}\' {sec}"')
