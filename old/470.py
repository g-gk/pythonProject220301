# Таблица

class Table:
    def __init__(self, rows, cols):
        self.table = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        if self.table and 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        if self.table:
            return len(self.table)
        return 0

    def n_cols(self):
        if self.table:
            return len(self.table[0])
        return 0


def main():
    print('Пример 1')
    tab = Table(3, 5)
    tab.set_value(0, 1, 10)
    tab.set_value(1, 2, 20)
    tab.set_value(2, 3, 30)
    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print('Пример 2')
    tab = Table(2, 2)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.set_value(0, 0, 10)
    tab.set_value(0, 1, 20)
    tab.set_value(1, 0, 30)
    tab.set_value(1, 1, 40)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()
    print('Пример 3')
    tab = Table(1, 1)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.set_value(0, 0, 1000)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()


if __name__ == '__main__':
    main()
