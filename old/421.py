from math import gcd

n = int(input())
a = [int(x) for x in input().split()]
mx = 0
for i in range(n):
    cur = a[i]
    p = 0
    if n - i < mx:
        break
    for j in range(i, n):
        p += 1
        cur = gcd(cur, a[j])
        if cur == 1:
            break
        a[j] //= cur
        if mx < p:
            mx = p
print(mx)
