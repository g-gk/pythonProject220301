# С занесением в список
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"


def main():
    points = [Point('A', 0, 3), Point('B', 4, 0)]
    print(points)
    print(points[0])
    print(repr(points[0]))

    print('-----------------')
    P = Point('P1', 12, 18)
    b = []
    for i in range(10):
        s = repr(P).split(',')
        s = s[0] + ', ' + str(i) + ', ' + str(2 * i) + ')'
        A = eval(s)
        b.append(A)
    print(b)

    even = []
    for p in b:
        if p.get_x() % 2 == 0 and p.get_y() % 2 == 0:
            even.append(p)
    print(even)

    for p in even:
        print(repr(p))


if __name__ == '__main__':
    main()
