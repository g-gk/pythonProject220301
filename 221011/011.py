from fractions import Fraction

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    ab = Fraction(a, b)
    cd = Fraction(c, d)
    ab0 = ab.numerator
    ab1 = ab.denominator
    cd0 = cd.numerator
    cd1 = cd.denominator
    if ab == cd:
        print(0)
    elif ab0 == 0 or cd0 == 0:
        print(1)
    else:
        xy = Fraction(ab / cd)
        xy0 = xy.numerator
        xy1 = xy.denominator
        if xy0 == 1 or xy1 == 1:
            print(1)
        else:
            print(2)
