# Банковские счета
n = int(input())
d = {}
for _ in range(n):
    op = input().split()
    if op[0] == 'DEPOSIT':
        d[op[1]] = d.get(op[1], 0) + int(op[2])
    elif op[0] == 'WITHDRAW':
        d[op[1]] = d.get(op[1], 0) - int(op[2])
    elif op[0] == 'BALANCE':
        if op[1] in d:
            print(d[op[1]])
        else:
            print('ERROR')
    elif op[0] == 'TRANSFER':
        d[op[1]] = d.get(op[1], 0) - int(op[3])
        d[op[2]] = d.get(op[2], 0) + int(op[3])
    elif op[0] == 'INCOME':
        for k, v in d.items():
            if v > 0:
                d[k] += int(d[k] * int(op[1]) / 100)
