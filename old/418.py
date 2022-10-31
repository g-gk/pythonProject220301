from math import factorial


def factor(n):
    res = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            res += [i]
            n //= i
        else:
            i += 1
    if n > 1:
        res += [n]
    return res


n = int(input())
if n == 1:
    print(1)
else:
    primes = factor(factorial(n))
    ans, num, cur = 1, 1, primes[0]
    for el in primes[1:]:
        if el == cur:
            num += 1
        else:
            ans *= num + 1
            num = 1
            cur = el
    ans *= num + 1
    print(ans)
