# Сложение многочленов

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(self.coefficients[i] * x ** i for i in range(len(self.coefficients)))

    def __add__(self, other):
        a, b = self.coefficients, other.coefficients
        res = []
        mx = max(len(a), len(b))
        for i in range(mx):
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0
            res += [x + y]
        return Polynomial(res)


def main():
    print('----- Пример 1 -----')
    poly = Polynomial([10, -1])
    print(poly(0))
    print(poly(1))
    print(poly(2))

    print('----- Пример 2 -----')
    poly1 = Polynomial([0, 0, 1])
    print(poly1(-2))
    print(poly1(-1))
    print(poly1(0))
    print(poly1(1))
    print(poly1(2))
    print()

    poly2 = Polynomial([0, 0, 2])
    print(poly2(-2))
    print(poly2(-1))
    print(poly2(0))
    print(poly2(1))
    print(poly2(2))
    print()

    poly3 = poly1 + poly2
    print(poly3(-2))
    print(poly3(-1))
    print(poly3(0))
    print(poly3(1))
    print(poly3(2))
    print()

    print('----- Пример 3 -----')
    poly1 = Polynomial([0, 1])
    poly2 = Polynomial([10])
    poly3 = poly1 + poly2
    poly4 = poly2 + poly1

    print(poly3(-2), poly4(-2))
    print(poly3(-1), poly4(-1))
    print(poly3(0), poly4(0))
    print(poly3(1), poly4(1))
    print(poly3(2), poly4(2))
    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
