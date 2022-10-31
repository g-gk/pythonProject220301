with open('input.txt') as f:
    data = f.read()
with open('output.txt', 'w') as f:
    f.write(str(sum(map(int, data.split()))))
