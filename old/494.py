# Классификация животных

class Shape:
    pass


class Polygon(Shape):
    pass


class Quadrilateral(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class Rectangle(Parallelogram):
    pass


class Square(Rectangle):
    pass


class Triangle(Polygon):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(IsoscelesTriangle):
    pass


def main():
    print('----- Пример 1 -----')

    print('----- Пример 2 -----')

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
