# Иерархия транспортных средств

class Transport:
    pass


class Ground(Transport):
    pass


class Railway(Transport):
    pass


class Water(Transport):
    pass


class Air(Transport):
    pass


class Ship(Water):
    pass


class Yacht(Water):
    pass


class Tanker(Water):
    pass


class Fighter(Air):
    pass


class Reactive(Air):
    pass


class Car(Ground):
    pass


def main():
    print('----- Пример 1 -----')

    print('----- Пример 2 -----')

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
