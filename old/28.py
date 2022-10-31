class TicTacToeBoard:
    # инициализатор
    def __init__(self):
        # переменная, которая отвечает за ходы. Когда эта переменная равна
        # четному числу ходит x, а когда нечетному - 0
        self.ch = 0
        # игровое поле, записанное в двумерном массиве
        self.pole = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        # статус игры, пусть игра завершена, когда статус равен 1, а когда 0 - игра в процессе
        self.status_play = 0

    # получение поля
    def get_field(self):
        return self.pole

    # создание новой игры
    def new_game(self):
        self.status_play = 0
        self.ch = 0
        self.pole = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def check_field(self):
        # проверяем, есть ли победитель на одной из горизонталей
        for y in range(3):
            if self.pole[y][0] != '-' and self.pole[y][0] == self.pole[y][1] == self.pole[y][2]:
                if self.pole[y][0] == 'X':
                    return 'X'
                elif self.pole[y][0] == '0':
                    return '0'
        # проверяем, есть ли победитель на одной из вертикалей
        for x in range(3):
            if self.pole[0][x] == self.pole[1][x] == self.pole[2][x] and self.pole[0][x] != '-':
                if self.pole[0][x] == 'X':
                    return 'X'
                elif self.pole[0][x] == '0':
                    return '0'
        # проверяем, есть ли победитель на 1 диагонали
        if self.pole[0][0] == self.pole[1][1] == self.pole[2][2] and self.pole[0][0] != '-':
            if self.pole[0][0] == 'X':
                return 'X'
            elif self.pole[0][0] == '0':
                return '0'
        # проверяем, есть ли победитель на 2 диагонали
        if self.pole[0][2] == self.pole[1][1] == self.pole[2][0] and self.pole[1][1] != '-':
            if self.pole[0][2] == 'X':
                return 'X'
            elif self.pole[0][2] == '0':
                return '0'
        # проверяем, можно ли играть дальше
        for y in range(3):
            for x in range(3):
                if self.pole[y][x] == '-':
                    return None
        # играть дальше нельзя и нет победителя, значит ничья
        return 'D'

    def make_move(self, row, col):
        # провверка, не завершена ли игра
        if self.status_play == 0:
            # если клетка занята, сообщаем об этом
            if self.pole[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} уже занята'
            # если клетка свободна
            else:
                # проверяем, кто должен ходить, и "делаем" ход
                if self.ch % 2 == 0:
                    self.pole[row - 1][col - 1] = 'X'
                else:
                    self.pole[row - 1][col - 1] = '0'
                self.ch += 1
            # проверяем на продолжение игры
            if self.check_field() is None:
                return 'Продолжаем играть'
            # возвращаем победителя х и меняем статус игры на завершено
            elif self.check_field() == 'X':
                self.status_play = 1
                return 'Победил игрок X'
            # возвращаем победителя 0 и меняем статус игры на завершено
            elif self.check_field() == '0':
                self.status_play = 1
                return 'Победил игрок 0'
            # сообщаем о ничье и меняем статус игры на завершено
            else:
                self.status_play = 1
                return 'Ничья'
        # если игра завершена, сообщаем об этом
        else:
            return 'Игра уже завершена'


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
