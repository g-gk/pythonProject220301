# Морской бой
class SeaMap:
    def __init__(self):
        self.map = [['.'] * 12 for _ in range(12)]

    def shoot(self, row, col, result):
        row += 1
        col += 1
        if result == 'miss':
            self.map[row][col] = '*'
        elif result == 'hit':
            self.map[row][col] = 'x'
        if result == 'sink':
            self.map[row][col] = 'x'
            x, y = row, col
            while self.map[x][y] == 'x':
                x -= 1
            x += 1
            while self.map[x][y] == 'x':
                y -= 1
            y += 1
            x1, y1 = x - 1, y - 1
            while self.map[x][y] == 'x':
                x += 1
            x -= 1
            while self.map[x][y] == 'x':
                y += 1
            y -= 1
            x2, y2 = x + 1, y + 1
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if self.map[x][y] != 'x':
                        self.map[x][y] = '*'

    def cell(self, row, col):
        return self.map[row + 1][col + 1]


def main():
    print('Пример 1')
    sm = SeaMap()
    sm.shoot(2, 0, 'miss')
    sm.shoot(6, 9, 'miss')
    for row in range(10):
        for col in range(10):
            print(sm.cell(row, col), end='')
        print()
    print('Пример 2')
    sm = SeaMap()
    sm.shoot(2, 0, 'sink')
    sm.shoot(6, 9, 'hit')
    for row in range(10):
        for col in range(10):
            print(sm.cell(row, col), end='')
        print()
    print('Пример 3')
    sm = SeaMap()
    sm.shoot(0, 0, 'sink')
    sm.shoot(0, 9, 'sink')
    sm.shoot(9, 0, 'sink')
    sm.shoot(9, 9, 'sink')
    for row in range(10):
        for col in range(10):
            print(sm.cell(row, col), end='')
        print()


if __name__ == '__main__':
    main()
