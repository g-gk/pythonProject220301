# Статистика
class Base:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)


class MinStat(Base):
    def result(self):
        if self.values:
            return min(self.values)


class MaxStat(Base):
    def result(self):
        if self.values:
            return max(self.values)


class AverageStat(Base):
    def result(self):
        if self.values:
            return sum(self.values) / len(self.values)


def main():
    print('Пример 1')
    values = [1, 2, 4, 5]

    mins = MinStat()
    maxs = MaxStat()
    average = AverageStat()
    for v in values:
        mins.add_number(v)
        maxs.add_number(v)
        average.add_number(v)

    print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
    print('Пример 2')
    mins = MinStat()
    maxs = MaxStat()
    average = AverageStat()

    print(mins.result(), maxs.result(), average.result())
    print('Пример 3')
    values = [1, 0, 0]

    mins = MinStat()
    maxs = MaxStat()
    average = AverageStat()
    for v in values:
        mins.add_number(v)
        maxs.add_number(v)
        average.add_number(v)

    print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


if __name__ == '__main__':
    main()
