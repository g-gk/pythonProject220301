from math import pi


class Shape:
    def describe(self):
        print(f'Класс: {self.__class__.__name__}')


class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return pi * self.r ** 2

    def square(self):
        side = pi ** 0.5 * self.r
        return Rectangle(side, side)


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


shape = Shape()
shape.describe()

circle = Circle(1)
circle.describe()

rectangle = Rectangle(1, 2)
rectangle.describe()

square = circle.square()
print(f'Площадь круга: {circle.area()}')
print(f'Площадь квадрата: {square.area()}')
print(f'Радиус круга: {circle.r}')
print(f'Длина стороны квадрата: {square.a}')
