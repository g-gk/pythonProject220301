from math import factorial, gcd, lcm

f40 = factorial(3)
f45 = factorial(8)
print(f40)
print(f45)
sab = set()
cnt = 0
for a in range(f40, f45):
    for b in range(a + 1, f45 + 1):
        if gcd(a, b) == f40 and lcm(a, b) == f45:
            cnt += 1
            print(cnt, a, b)
            sab.add((a, b))

print()
