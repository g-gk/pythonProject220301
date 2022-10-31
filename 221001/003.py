import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 50)
        self.setWindowTitle('Фокус со словами')

        self.input1 = QLineEdit(self)
        self.input1.setFixedWidth(100)

        self.btn = QPushButton('->', self)
        self.btn.setFixedWidth(30)

        self.input2 = QLineEdit(self)
        self.input2.setFixedWidth(100)

        w1 = self.input1.width()
        w2 = self.btn.width()

        self.input1.move(10, 10)
        self.btn.move(w1 + 10, 10)
        self.input2.move(w1 + w2 + 10, 10)
        self.btn.clicked.connect(self.a)

    def a(self):
        t = self.btn.text()
        if t == '<-':
            self.input1.setText(self.input2.text())
            self.input2.setText('')
            self.btn.setText('->')
        else:
            self.input2.setText(self.input1.text())
            self.input1.setText('')
            self.btn.setText('<-')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
