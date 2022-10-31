WHITE = 0
BLACK = 1


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


class Figure:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color


class Queen(Figure):
    def __init__(self, row, col, color):
        super(Queen, self).__init__(row, col, color)

    def char(self):
        return 'Q'

    def can_move(self, row, col):
        if 0 > row or row > 7 or 7 < col or col < 0:
            return False
        if abs(self.row - row) == abs(self.col - col):
            return True
        if self.row == row or self.col == col:
            return True
        return False


class Bishop(Figure):
    def __init__(self, row, col, color):
        super(Bishop, self).__init__(row, col, color)

    def char(self):
        return 'B'

    def can_move(self, row, col):
        if 0 > row or row > 7 or 7 < col or col < 0:
            return False
        if abs(self.row - row) == abs(self.col - col):
            return True
        return False


class Knight(Figure):
    def __init__(self, row, col, color):
        super(Knight, self).__init__(row, col, color)

    def char(self):
        return 'N'

    def can_move(self, row, col):
        if 0 > row or row > 7 or 7 < col or col < 0:
            return False
        if abs(row - self.row) > 2 and abs(col - self.col) > 2:
            return False
        if (abs(self.row - row) == 2 and abs(self.col - col) == 1) or \
                (abs(self.row - row) == 1 and abs(self.col - col) == 2):
            return True
        return False


class Pawn(Figure):
    def __init__(self, row, col, color):
        super(Pawn, self).__init__(row, col, color)

    def char(self):
        return 'P'

    def can_move(self, row, col):
        if self.col != col:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.row + direction == row:
            return True
        if self.row == start_row and self.row + 2 * direction == row:
            return True
        return False


class Rook(Figure):
    def __init__(self, row, col, color):
        super(Rook, self).__init__(row, col, color)

    def char(self):
        return 'R'

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

    def current_player_color(self):
        return self.color

    def is_under_attack(self, row, col, color):
        for i in range(len(self.field)):
            t = False
            for j in range(len(self.field[i])):
                if self.field[i][j]:
                    figure = self.field[i][j]
                    if figure.get_color() == color:
                        t = figure.can_move(row, col)
                if t:
                    return True

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True


def main():
    board = Board()

    board.field = [([None] * 8) for i in range(8)]
    board.field[0][0] = Rook(0, 0, WHITE)
    board.field[1][2] = Bishop(1, 2, WHITE)
    coords = ((0, 0), (1, 2))

    print('White:')
    for row in range(7, -1, -1):
        for col in range(8):
            if (row, col) in coords:
                print('W', end='')
            elif board.is_under_attack(row, col, WHITE):
                print('x', end='')
            else:
                print('-', end='')
        print()

        board = Board()

        board.field = [([None] * 8) for i in range(8)]
        board.field[0][5] = Rook(0, 5, WHITE)
        board.field[1][2] = Bishop(1, 2, WHITE)
        board.field[7][6] = Knight(7, 6, WHITE)
        coords = ((0, 5), (1, 2), (7, 6))

        print('White:')
        for row in range(7, -1, -1):
            for col in range(8):
                if (row, col) in coords:
                    print('W', end='')
                elif board.is_under_attack(row, col, WHITE):
                    print('x', end='')
                else:
                    print('-', end='')
            print()

        board = Board()

        board.field = [([None] * 8) for i in range(8)]
        board.field[0][5] = Rook(0, 5, WHITE)
        board.field[1][2] = Bishop(1, 2, WHITE)
        board.field[7][6] = Knight(7, 6, BLACK)
        w_coords = ((0, 5), (1, 2))
        b_coords = ((7, 6),)

        print('White:')
        for row in range(7, -1, -1):
            for col in range(8):
                if (row, col) in w_coords:
                    print('W', end='')
                elif board.is_under_attack(row, col, WHITE):
                    print('x', end='')
                else:
                    print('-', end='')
            print()
        print()

        print('Black:')
        for row in range(7, -1, -1):
            for col in range(8):
                if (row, col) in b_coords:
                    print('B', end='')
                elif board.is_under_attack(row, col, BLACK):
                    print('x', end='')
                else:
                    print('-', end='')
            print()


if __name__ == '__main__':
    main()
