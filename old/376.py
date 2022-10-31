# На завод!
def sq(n):
    res = 1
    while res * res <= n:
        res += 1
    return (res - 1) * (res - 1)


x = int(input())
y = int(input())
s1 = sq(x) + sq(y)
s2 = sq(x + y)
if s1 > s2:
    print('Petya leaves paint to himself')
elif s1 < s2:
    print('Petya gives paint to Vasya')
else:
    print('Equal')
