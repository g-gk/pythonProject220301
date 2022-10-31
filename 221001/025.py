import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QRadioButton, QButtonGroup

SymbolX = 'X'
Symbol0 = '0'


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # парметры QWidget
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Крестики-нолики')

        # выбор символа для хода
        self.QRadioButtonX = QRadioButton(SymbolX, self)
        self.QRadioButtonX.setChecked(True)
        self.QRadioButtonX.move(20, 10)

        self.QRadioButtonO = QRadioButton(Symbol0, self)
        self.QRadioButtonO.move(120, 10)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.QRadioButtonX)
        self.button_group.addButton(self.QRadioButtonO)

        self.btn1 = QPushButton('Новая игра', self)
        self.btn1.setFixedSize(100, 25)
        self.btn1.move(50, 200)
        self.btn1.clicked.connect(self.new_game)

        self.lable = QLabel(self)
        self.lable.setFixedWidth(100)
        self.lable.move(75, 170)

        # поле кнопок
        x, y = 40, 40
        w, h = 40, 40
        self.map = []
        for row_index in range(3):
            row = []
            for column_index in range(3):
                btn = QPushButton(self)
                btn.setFixedSize(w, h)
                btn.move(x + row_index * w, y + column_index * h)
                btn.clicked.connect(self.a)
                row.append(btn)
            self.map.append(row)

    def new_game(self):
        # очистить лейбл результата игры
        self.lable.setText('')
        for row in self.map:
            for btn in row:
                btn: QPushButton
                btn.setText('')
                btn.setEnabled(True)

    def a(self):
        btn: QPushButton = self.sender()
        t = btn.text()
        if not t:
            t = self.button_group.checkedButton().text()
            btn.setText(t)
        # порверка на победу или ничью
        res = self.check_field()
        if res:
            # вывести кто победитель или ничья на соответствующий лейбл
            if res == 'Ничья!':
                self.lable.setText(res)
            else:
                self.lable.setText(f'Выиграл {res}!')
            for row in self.map:
                for btn in row:
                    btn: QPushButton
                    btn.setEnabled(False)
        # print(f'res={res}')

    def check_field(self):
        # проверить х и 0 в строках
        for row in self.map:
            line_str = ''.join([x.text() for x in row])
            if line_str == SymbolX * len(row):
                return SymbolX
            elif line_str == Symbol0 * len(row):
                return Symbol0
        # проверить х и 0 в столбцах
        for t in range(3):
            stolb = [self.map[i][t] for i in range(3)]
            line_str = ''.join([x.text() for x in stolb])
            if line_str == SymbolX * len(stolb):
                return SymbolX
            elif line_str == Symbol0 * len(stolb):
                return Symbol0
        # проверить х и 0 в диагоналях
        diag1 = [self.map[i][i] for i in range(3)]
        line_str = ''.join([x.text() for x in diag1])
        if line_str == SymbolX * len(diag1):
            return SymbolX
        elif line_str == Symbol0 * len(diag1):
            return Symbol0
        diag2 = [self.map[i][2 - i] for i in range(3)]
        line_str = ''.join([x.text() for x in diag2])
        if line_str == SymbolX * len(diag2):
            return SymbolX
        elif line_str == Symbol0 * len(diag2):
            return Symbol0
        if len(''.join(''.join([x.text() for x in h]) for h in self.map)) == 9:
            return 'Ничья!'
        return ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
