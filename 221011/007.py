import sys
from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class WordFocus(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 50)
        self.setWindowTitle('Случайная Строка')

        self.btn = QPushButton(self)
        self.btn.move(0, 5)
        self.btn.resize(100, 40)
        self.btn.setText("Получить")
        self.btnpos = 0
        self.btn.clicked.connect(self.run)

        self.str = QLineEdit(self)
        self.str.move(115, 15)
        self.str.resize(200, 25)

    def run(self):
        with open('cyrillic.txt') as f:
            text = f.readlines()
        a = randint(0, len(text))
        if text:
            print(text[a])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wf = WordFocus()
    wf.show()
    sys.exit(app.exec())
