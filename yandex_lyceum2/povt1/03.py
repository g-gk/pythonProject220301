# ГЕЗ, ЩЗКГУЯ!
lines = [''] * 3
lines[1] = input()
n = len(lines[1])
shift = int(input()) % n
lines[0] = lines[1][shift:] + lines[1][:shift]
lines[2] = lines[1][-shift:] + lines[1][:-shift]
for line in lines:
    print(line)
