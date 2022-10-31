n = int(input())
d = 0
while n % 2 == 0:
    d += 1
    n //= 2
a = [2] * d
a[-1] *= n
if d == 1:
    print("prime")
else:
    for x in range(3, int(n ** 0.5) + 1, 2):
        if not (n % x):
            b = a[:]
            b[-1] //= x
            b[-2] *= x
            print("many")
            print(*a)
            print(*b)
            exit(0)
    print("single")
    print(*a)
