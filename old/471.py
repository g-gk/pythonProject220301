# Прямоугольники

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):
        x1, y1, w1, h1 = self.x, self.y, self.w, self.h
        x2, y2, w2, h2 = other.x, other.y, other.w, other.h
        if x1 < x2:
            if y1 < y2:
                if x1 + w1 > x2 and y1 + h1 > y2:
                    if x1 + w1 < x2 + w2 and y1 + h1 < y2 + h2:
                        if x1 + w1 - x2 and y1 + h1 - y2:
                            return Rectangle(x2, y2, x1 + w1 - x2, y1 + h1 - y2)
                    else:
                        return Rectangle(x2, y2, w2, h2)
            else:
                if x2 < x1 + w1 and y1 < y2 + h2:
                    w, h = x1 + w1 - x2, y2 + h2 - y1
                    if w and h:
                        return Rectangle(x2, y1, w, h)
        else:
            x1, y1, w1, h1, x2, y2, w2, h2 = x2, y2, w2, h2, x1, y1, w1, h1
            if y1 < y2:
                if x1 + w1 > x2 and y1 + h1 > y2:
                    if x1 + w1 < x2 + w2 and y1 + h1 < y2 + h2:
                        if x1 + w1 - x2 and y1 + h1 - y2:
                            return Rectangle(x2, y2, x1 + w1 - x2, y1 + h1 - y2)
                    else:
                        return Rectangle(x2, y2, w2, h2)
            else:
                if x2 < x1 + w1 and y1 < y2 + h2:
                    w, h = x1 + w1 - x2, y2 + h2 - y1
                    if w and h:
                        return Rectangle(x2, y1, w, h)


def main():
    print('Пример 1')
    rect1 = Rectangle(0, 0, 10, 10)
    rect2 = Rectangle(5, 5, 10, 10)
    rect3 = rect1.intersection(rect2)

    if rect3 is None:
        print('No intersection')
    else:
        print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
    print('Пример 2')
    rect1 = Rectangle(0, 0, 10, 10)
    rect2 = Rectangle(10, 0, 10, 10)
    rect3 = rect1.intersection(rect2)

    if rect3 is None:
        print('No intersection')
    else:
        print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
    print('Пример 3')
    rect1 = Rectangle(3, 5, 2, 1)
    rect2 = Rectangle(1, 2, 10, 10)
    rect3 = rect1.intersection(rect2)

    if rect3 is None:
        print('No intersection')
    else:
        print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())


if __name__ == '__main__':
    main()
