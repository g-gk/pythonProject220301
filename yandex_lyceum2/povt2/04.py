# Точка обыкновенная
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y


def main():
    print('---------- Пример 1 ----------')
    point = Point(3, -4)
    print(point.get_x())
    print(point.get_y())
    print(point.get_coords())

    print('---------- Пример 2 ----------')


if __name__ == '__main__':
    main()
