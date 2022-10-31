# Именованная точка
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


def main():
    print('---------- Пример 1 ----------')
    point_A = Point('A', 3, -4)
    print(point_A)
    point_B = ~point_A
    print(point_B)
    print(~Point('O', 0, 0))

    print('---------- Пример 2 ----------')


if __name__ == '__main__':
    main()
