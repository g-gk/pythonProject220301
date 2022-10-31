# О колоколах подробнее

class Bell:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        # print(self.kwargs)

    def print_info(self):
        if self.args and self.kwargs:
            print(', '.join(f'{k}: {self.kwargs[k]}' for k in sorted(self.kwargs.keys())) +
                  '; ' + ', '.join(self.args))
        elif self.args:
            print(', '.join(self.args))
        elif self.kwargs:
            print(', '.join(f'{k}: {self.kwargs[k]}' for k in sorted(self.kwargs.keys())))
        else:
            print('-')


class LittleBell(Bell):
    def __init__(self, *args, **kwargs):
        super(LittleBell, self).__init__(*args, **kwargs)

    def sound(self):
        print('ding')


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super(BigBell, self).__init__(*args, **kwargs)
        self.f = True

    def sound(self):
        if self.f:
            print('ding')
        else:
            print('dong')
        self.f = not self.f


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')


def main():
    print('---------- Пример 1 ----------')
    Bell("бронзовый").print_info()
    LittleBell("медный", нота="ля").print_info()
    BigBell(название="Корноухий", вес="1275 пудов").print_info()

    print('---------- Пример 2 ----------')
    BigBell("крупнейший в мире действующий колокол", название="Bell of Good Luck",
            высота="810,8 см", диаметр="511,8 см", вес="116 тонн").print_info()
    LittleBell().print_info()


if __name__ == '__main__':
    main()
