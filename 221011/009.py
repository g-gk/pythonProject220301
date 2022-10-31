import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel, QLineEdit


class slova(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 320, 80)
        self.setWindowTitle('Случайная строка из файла — 2')

        self.btn = QPushButton('->', self)
        self.btn.resize(25, 25)
        self.btn.move(20, 25)
        self.btn.clicked.connect(self.stroch)

        self.name_input1 = QLineEdit(self)
        self.name_input1.resize(250, 25)
        self.name_input1.move(50, 25)

    def stroch(self):
        with open('lines.txt') as f:
            text = f.readlines()

        if text:
            a = randint(0, len(text) - 1)
            self.name_input1.setText(text[a])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = slova()
    ex.show()
    sys.exit(app.exec())
