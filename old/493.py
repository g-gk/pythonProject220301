# Классификация животных

class Animal:
    def breathe(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass


def main():
    print('----- Пример 1 -----')

    print('----- Пример 2 -----')

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
