# Для галочки
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
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)

    def __ge__(self, other):
        return (self.x, self.y) >= (other.x, other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)


class CheckMark(Point):
    def __init__(self, *points):
        self.points = points
        # print(points)

    def __str__(self):
        res = ''
        for p in self.points:
            res += p.name
        return res

    def __eq__(self, other):
        return self.points[1] == other.points[1] and (
                self.points[0] == other.points[0] and self.points[2] == other.points[2] or
                self.points[0] == other.points[2] and self.points[2] == other.points[0])

    def __ne__(self, other):
        return not __eq__(self, other)

    def __bool__(self):
        return not (self.points[0].x == self.points[1].x or self.points[0].x != self.points[2].x or
                    self.points[1].x == self.points[2].x
                    or self.points[0].y == self.points[1].y or self.points[0].y != self.points[
                        2].y or self.points[1].y == self.points[2].y)


def main():
    print('Пример 1')
    p_A = Point('A', 1, 2)
    p_B = Point('B', 0, 1)
    p_C = Point('C', -1, 2)
    p_D = Point('D', 2, 2)
    p_E = Point('E', 2, 0)
    p_F = Point('F', 2, -1)
    cm_ABC = CheckMark(p_A, p_B, p_C)
    cm_DEF = CheckMark(p_D, p_E, p_F)
    cm_ABB = CheckMark(p_A, p_B, p_B)
    print(cm_ABC, bool(cm_ABC))
    print(cm_DEF, bool(cm_DEF))
    print(cm_ABB, bool(cm_ABB))

    print('Пример 2')
    p_A = Point('A', 1, 2)
    p_B = Point('B', 0, 1)
    p_C = Point('C', -1, 2)
    p_D = Point('D', -1, 2)
    cm_ABC = CheckMark(p_A, p_B, p_C)
    cm_CBA = CheckMark(p_C, p_B, p_A)
    cm_ACB = CheckMark(p_A, p_C, p_B)
    cm_ABD = CheckMark(p_A, p_B, p_D)
    cm_DBA = CheckMark(p_D, p_B, p_A)
    print(cm_ABC == cm_CBA, cm_ABC == cm_ABD)
    print(cm_ABC == cm_DBA, cm_ABC == cm_ACB)


if __name__ == '__main__':
    main()
