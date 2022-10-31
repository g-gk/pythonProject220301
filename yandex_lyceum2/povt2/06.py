# Осторожно окрашенные
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class ColoredPoint(Point):
    def __init__(self, name, x, y, color=(0, 0, 0)):
        super(ColoredPoint, self).__init__(name, x, y)
        self.color = color

    def get_color(self):
        return self.color

    def __invert__(self):
        invert_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        return ColoredPoint(self.name, self.y, self.x, invert_color)


def main():
    print('---------- Пример 1 ----------')
    point_X = Point('X', 5, -7)
    print(point_X)
    point_A = ColoredPoint('A', 0, 3, (255, 204, 0))
    print(point_A, point_A.get_color())
    point_B = ~point_A
    print(point_B, point_B.get_color())
    point_O = ~ColoredPoint('O', 0, 0)
    print(point_O, point_O.get_color())

    print('---------- Пример 2 ----------')


if __name__ == '__main__':
    main()
