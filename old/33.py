# Квадратичная функция
class SquareFunction:
    def __init__(self, *args):
        self.a, self.b, self.c = args

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


# sf = SquareFunction(1, 0, 0)
# print(sf(-2))
# print(sf(-1))
# print(sf(-0))
# print(sf(1))
# print(sf(2))
# print(sf(10))

# sf = SquareFunction(1, 2, 1)
# print(sf(-2))
# print(sf(-1))
# print(sf(-0))
# print(sf(1))
# print(sf(2))
# print(sf(10))

# sf = SquareFunction(0, 0, 1)
# print(sf(-2))
# print(sf(-1))
# print(sf(-0))
# print(sf(1))
# print(sf(2))
# print(sf(10))
