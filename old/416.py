from math import factorial

n = int(input())
nf = factorial(n)
sqrtnf = int(nf ** 0.5)
cnt = 2
for d in range(2, sqrtnf + 1):
    if nf % d == 0:
        cnt += 2
if sqrtnf ** 2 == n:
    cnt -= 1
print(cnt)
