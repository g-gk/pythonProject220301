class TicTacToeBoard:
    def __init__(self):
        self.map = [['-' for _ in range(3)] for __ in range(3)]
        self.next_step = 'X'
        self.winn = None

    def new_game(self):
        self.map = [['-' for _ in range(3)] for __ in range(3)]
        self.next_step = 'X'
        self.winn = None

    def get_field(self):
        return self.map

    def check_field(self):
        for line in self.map:
            line_str = ''.join(line)
            if line_str == 'XXX':
                return 'X'
            elif line_str == '000':
                return '0'

        # проверить х и 0 в столбцах
        for t in range(3):
            stolb = [self.map[i][t] for i in range(3)]
            line_str = ''.join(stolb)
            if line_str == 'XXX':
                self.winn = 'X'
                return 'X'
            elif line_str == '000':
                self.winn = '0'
                return '0'
        # проверить х и 0 в диагоналях
        diag1 = [self.map[i][i] for i in range(3)]
        line_str = ''.join(diag1)
        if line_str == 'XXX':
            self.winn = 'X'
            return 'X'
        elif line_str == '000':
            self.winn = '0'
            return '0'
        diag2 = [self.map[i][2 - i] for i in range(3)]
        line_str = ''.join(diag2)
        if line_str == 'XXX':
            self.winn = 'X'
            return 'X'
        elif line_str == '000':
            self.winn = '0'
            return '0'
        if '-' in ''.join(''.join(h) for h in self.map):
            return 'None'
        self.winn = 'D'
        return 'D'

    def make_move(self, row, col):
        row -= 1
        col -= 1
        if self.winn is not None:
            return 'Игра уже завершена'
        if self.map[row][col] == '-':
            self.map[row][col] = self.next_step
            if self.next_step == 'X':
                self.next_step = '0'
            else:
                self.next_step = 'X'
            res = self.check_field()
            if res == 'X':
                return 'Победил игрок X'
            elif res == '0':
                return 'Победил игрок 0'
            elif res == 'D':
                return 'Ничья'
            elif res == 'None':
                return 'Продолжаем играть'
        else:
            return f'Клетка {row + 1}, {col + 1} уже занята'


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
