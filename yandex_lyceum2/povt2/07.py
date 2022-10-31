# Колокольня
class LittleBell:
    def sound(self):
        print('ding')


class BigBell:
    def __init__(self):
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
    bell_tower = BellTower(BigBell(), LittleBell())
    bell_tower.sound()
    bell_tower.sound()
    bell_tower.append(BigBell())
    bell_tower.sound()
    bell_tower.sound()

    print('---------- Пример 2 ----------')
    bell_tower = BellTower()
    bell_tower.sound()
    bell_tower.append(BigBell())
    bell_tower.sound()
    bell_tower.append(BigBell())
    bell_tower.sound()


if __name__ == '__main__':
    main()
