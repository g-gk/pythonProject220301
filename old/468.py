# Класс крестики-нолики
class TicTacToeBoard:
    def __init__(self):
        self.field = [['-'] * 3 for _ in range(3)]
        self.player = ['X', '0']
        self.cur = False
        self.end = False

    def new_game(self):
        self.field = [['-'] * 3 for _ in range(3)]
        self.cur = False
        self.end = False

    def get_field(self):
        return self.field

    def check_field(self):
        f = [False, False]
        for i in range(2):
            ci = self.player[i] * 3
            d1 = ''.join(self.field[t][t] for t in range(3))
            d2 = ''.join(self.field[t][2 - t] for t in range(3))
            for j in range(3):
                r = ''.join(self.field[j])
                c = ''.join(self.field[t][j] for t in range(3))
                if r == ci or c == ci or d1 == ci or d2 == ci:
                    f[i] = True
        if f[0] and f[1]:
            self.end = True
            return 'D'
        elif f[0]:
            self.end = True
            return 'X'
        elif f[1]:
            self.end = True
            return '0'

    def make_move(self, row, col):
        if self.end:
            return 'Игра уже завершена'
        if self.field[row - 1][col - 1] == '-':
            self.field[row - 1][col - 1] = self.player[self.cur]
            self.cur = not self.cur
        else:
            return f'Клетка {row}, {col} уже занята'
        res = self.check_field()
        if res == 'X':
            return 'Победил игрок X'
        elif res == '0':
            return 'Победил игрок 0'
        elif res == 'D':
            return 'Ничья'
        return 'Продолжаем играть'


def main():
    print('Пример 1')
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
    print('Пример 2')
    board = TicTacToeBoard()
    print(*board.get_field(), sep="\n")
    print(board.make_move(1, 1))
    board.new_game()
    print(*board.get_field(), sep="\n")
    print(board.make_move(1, 1))
    print(board.make_move(1, 2))
    print(*board.get_field(), sep="\n")
    print(board.make_move(3, 1))
    print(board.make_move(2, 2))
    print(board.make_move(3, 1))
    print(board.make_move(2, 3))
    print(board.make_move(3, 2))
    print(*board.get_field(), sep="\n")
    print('Пример 3')


if __name__ == '__main__':
    main()
