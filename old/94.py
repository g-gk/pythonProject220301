class Chess:
    def __init__(self, col, row, collor):
        self.col = col
        self.row = row
        self.collor = collor


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Knight(Chess):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.field = list()
        for i in range(8):
            x = ['-' for j in range(8)]
            self.field.append(x)

    def can_move(self, row1, col1):
        if correct_coords(row1, col1):
            if self.row + 2 == row1 and self.col + 1 == col1:
                return True
            if self.row + 2 == row1 and self.col - 1 == col1:
                return True
            if self.row - 2 == row1 and self.col + 1 == col1:
                return True
            if self.row - 2 == row1 and self.col - 1 == col1:
                return True
            if self.row + 1 == row1 and self.col + 2 == col1:
                return True
            if self.row + 1 == row1 and self.col - 2 == col1:
                return True
            if self.row - 1 == row1 and self.col + 2 == col1:
                return True
            if self.row - 1 == row1 and self.col - 2 == col1:
                return True
            else:
                return False
        else:
            return False

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def set_position(self, row1, col1):
        if correct_coords(row1, col1):
            self.row = row1
            self.col = col1


class Bishop(Chess):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.field = list()
        for i in range(8):
            x = ['-' for j in range(8)]
            self.field.append(x)

    def can_move(self, row1, col1):
        if correct_coords(row1, col1):
            if row1 - self.row == col1 - self.col:
                return True
            if self.row - row1 == col1 - self.col:
                return True
            else:
                return False
        else:
            return False

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def set_position(self, row1, col1):
        if correct_coords(row1, col1):
            self.row = row1
            self.col = col1


class Queen(Chess):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.field = list()
        for i in range(8):
            x = ['-' for j in range(8)]
            self.field.append(x)

    def can_move(self, row1, col1):
        if correct_coords(row1, col1):
            a = abs(row1 - self.row) == abs(col1 - self.col)
            b = self.row == row1 and self.col != col1
            c = self.row != row1 and self.col == col1
            return a or b or c

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def set_position(self, row1, col1):
        if correct_coords(row1, col1):
            self.row = row1
            self.col = col1