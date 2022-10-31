# Вычитание дат

class Date:
    def __init__(self, m, d):
        self.m = m
        self.d = d

    def __sub__(self, other):
        ms = list(range(1, 13))
        ds = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return (sum(ds[x] for x in range(self.m - 1)) + self.d -
                sum(ds[x] for x in range(other.m - 1)) - other.d)


def main():
    print('----- Пример 1 -----')
    jan5 = Date(1, 5)
    jan1 = Date(1, 1)

    print(jan5 - jan1)
    print(jan1 - jan5)
    print(jan1 - jan1)
    print(jan5 - jan5)

    print('----- Пример 2 -----')
    mar5 = Date(3, 1)
    jan1 = Date(1, 1)

    print(mar5 - jan1)
    print(jan1 - mar5)
    print(jan1 - jan1)
    print(mar5 - mar5)

    print('----- Пример 3 -----')
    jan31 = Date(1, 31)
    feb1 = Date(2, 1)
    feb2 = Date(2, 2)

    print(feb1 - jan31)
    print(jan31 - feb1)
    print(feb1 - feb1)
    print()

    print(feb2 - jan31)
    print(jan31 - feb2)
    print(feb2 - feb2)
    print()

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
