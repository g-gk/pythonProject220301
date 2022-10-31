# Равенство и порядок
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

    def __lt__(self, other):
        return (self.name, self.x, self.y) < (other.name, other.x, other.y)

    def __le__(self, other):
        return (self.name, self.x, self.y) <= (other.name, other.x, other.y)

    def __gt__(self, other):
        return (self.name, self.x, self.y) > (other.name, other.x, other.y)

    def __ge__(self, other):
        return (self.name, self.x, self.y) >= (other.name, other.x, other.y)

    def __eq__(self, other):
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)

    def __ne__(self, other):
        return (self.name, self.x, self.y) != (other.name, other.x, other.y)


def main():
    print('Пример 1')
    p_A1 = Point('A', 1, 2)
    p_A2 = Point('A', 2, 1)
    p_B1 = Point('B', 2, 3)
    p_B2 = Point('B', 2, 3)
    print(p_A1 == p_A2, p_B1 == p_B2)
    print(p_A1 != p_A2, p_B1 != p_B2)
    print(p_A1 < p_A2, p_B1 > p_B2)
    print(p_A1 >= p_A2, p_B1 <= p_B2)
    print(max(p_A1, p_B2, p_A2, p_B2))
    print(min(p_A1, p_B2, p_A2, p_B2))

    print('Пример 2')
    points = [Point('A', 101, 1), Point('B', -1, 0),
              Point('A', 11, 0), Point('A', 111, -11)]
    points.sort()
    print(', '.join(map(str, points)))


if __name__ == '__main__':
    main()
