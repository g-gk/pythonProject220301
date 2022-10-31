class TicTacToeBoard:
    def __init__(self):
        self.winner = None
        self.board = list()
        for i in range(3):
            a = list()
            for j in range(3):
                a.append('-')
            self.board.append(a)
        self.mot = 'X'

    def new_game(self):
        self.winner = None
        self.board = list()
        for i in range(3):
            a = list()
            for j in range(3):
                a.append('-')
            self.board.append(a)
        self.mot = 'X'

    def get_field(self):
        return self.board

    def make_move(self, row, col):
        row -= 1
        col -= 1
        if self.winner:
            return 'Игра уже завершена'
        if self.board[row][col] != '-':
            return f'Клетка {row + 1}, {col + 1} уже занята'
        else:
            self.board[row][col] = self.mot
            if self.mot == 'X':
                self.mot = '0'
            else:
                self.mot = 'X'
        x = self.check_field()
        if x:
            if x == 'D':
                return 'Ничья'
            else:
                return f'Победил игрок {x}'
        else:
            return 'Продолжаем играть'

    def check_field(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[2][i] == self.board[1][i] and \
                    self.board[2][i] == self.board[0][i] and not self.winner and self.board[0][
                i] != '-':
                self.winner = self.board[0][i]
            elif self.board[i][0] == self.board[i][1] and self.board[i][2] == self.board[i][1] and \
                    self.board[i][2] == self.board[i][0] and not self.winner and self.board[i][
                0] != '-':
                self.winner = self.board[i][0]
        if self.board[0][0] == self.board[1][1] and self.board[2][2] == self.board[1][1] and \
                self.board[2][2] == \
                self.board[0][0] and not self.winner and self.board[0][0] != '-':
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1] and \
                self.board[0][2] == \
                self.board[2][0] and not self.winner and self.board[0][2] != '-':
            self.winner = self.board[2][0]
        if not self.winner:
            self.winner = 'D'
            for i in self.board:
                if '-' in i:
                    self.winner = None
                    break
        return self.winner


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
