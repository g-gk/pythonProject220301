a = [int(input()) for _ in range(3)]
d = [a[1] - a[0], a[2] - a[1]]
if d[0] == d[1]:
    print(a[0] - d[0])
    print(1)
elif d[0] == 2 * d[1]:
    print(a[0] + d[1])
    print(2)
else:
    print(a[1] + d[0])
    print(3)
