# Таблица с изменяемым размером

class Table:
    def __init__(self, rows, cols):
        self.table = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        if self.table and 0 <= row < self.n_rows() and 0 <= col < self.n_cols():
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

    def delete_row(self, row):
        del self.table[row]

    def delete_col(self, col):
        for row in range(self.n_rows()):
            del self.table[row][col]

    def add_row(self, row):
        if row == self.n_rows():
            self.table += [[0] * self.n_cols()]
        elif 0 <= row < self.n_rows():
            self.table.insert(row, [0] * self.n_cols())

    def add_col(self, col):
        if col == self.n_cols():
            for row in range(self.n_rows()):
                self.table[row] += [0]
        elif 0 <= col < self.n_cols():
            for row in range(self.n_rows()):
                self.table[row].insert(col, 0)


def main():
    print('----- Пример 1 -----')
    tab = Table(3, 5)
    tab.set_value(0, 1, 10)
    tab.set_value(1, 2, 20)
    tab.set_value(2, 3, 30)
    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.add_row(1)

    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    print('----- Пример 2 -----')
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

    tab.add_row(0)
    tab.add_col(1)

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    print('----- Пример 3 -----')
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

    tab.add_row(0)
    tab.add_row(2)
    tab.add_col(0)
    tab.add_col(2)

    tab.set_value(0, 0, 2000)
    tab.set_value(0, 2, 3000)
    tab.set_value(2, 0, 4000)
    tab.set_value(2, 2, 5000)

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    print('----- Пример 4 -----')
    tab = Table(0, 0)

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

    tab.add_col(0)
    tab.add_row(0)
    tab.set_value(0, 0, 1000)

    for i in range(-1, tab.n_rows() + 1):
        for j in range(-1, tab.n_cols() + 1):
            print(tab.get_value(i, j), end=' ')
        print()
    print()


if __name__ == '__main__':
    main()
