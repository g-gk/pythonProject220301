s = 'egffe'
while len(s) < 47:
    s = s.replace('e', 'eff')
    print(s)
    s = s.replace('g', 'fef')
    print(s)
print(s)
print(len(s))
print(s.count('f'))  # 44
