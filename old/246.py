def gcd(n1, n2):
    if n1 < n2:
        return gcd(n2, n1)
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


n = int(input())
a = int(input())
b = int(input())
print(n // a + n // b - n // (a * b // gcd(a, b)))
