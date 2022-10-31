# Социальная сеть

class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        self.info()


class Person(User):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def info(self):
        return f'Дата рождения: {self.data}'

    def subscribe(self, user: User):
        pass


class Community(User):
    def __init__(self, name, describe):
        self.name = name
        self.describe = describe

    def info(self):
        return f'Описание: {self.describe}'


def main():
    print('----- Пример 1 -----')

    print('----- Пример 2 -----')

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
