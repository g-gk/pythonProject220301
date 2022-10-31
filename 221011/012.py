from math import factorial, log

n = factorial(100)
# print(n)
mx = int(log(n) / log(2)) + 2
my = int(log(n) / log(3)) + 2
mz = int(log(n) / log(5)) + 2
print(mx, my, mz)
# x2=2
# y3=3
# z5=5
for x in range(2, mx):
    for y in range(2, my):
        for z in range(2, mz):
            n1 = 2 ** x + 3 ** y + 5 ** z
            if n1 == n:
                print(x, y, z)
                exit(0)
            elif n1 > n:
                break
