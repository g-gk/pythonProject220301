n1 = int(input())
n2 = int(input())
n3 = int(input())
a = []
if n2 - n1 == n3 - n2:
    m = [1, 4]
else:
    m = [2, 3]
for el in m:
    if el == 1:
        a = [0, n1, n2, n3]
    elif el == 2:
        a = [n1, 0, n2, n3]
    elif el == 3:
        a = [n1, n2, 0, n3]
    elif el == 4:
        a = [n1, n2, n3, 0]
    b = a.copy()
    for i in range(200001):
        a[el - 1] = i
        if a[3] - a[2] == a[2] - a[1] == a[1] - a[0]:
            print(i)
            print(el)
            exit(0)
