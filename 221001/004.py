import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel, QLineEdit


class slova(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 320, 80)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton('->', self)
        self.btn.resize(25, 25)
        self.btn.move(150, 25)
        self.btn.clicked.connect(self.hello)

        self.name_input = QLineEdit(self)
        self.name_input.resize(125, 25)
        self.name_input.move(10, 25)

        self.name_input1 = QLineEdit(self)
        self.name_input1.resize(125, 25)
        self.name_input1.move(190, 25)

    def hello(self):
        if self.btn.text() == '->':
            self.btn.setText('<-')
            self.name_input1.setText(self.name_input.text())
            self.name_input.setText('')

        else:
            self.btn.setText('->')
            self.name_input.setText(self.name_input1.text())
            self.name_input1.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = slova()
    ex.show()
    sys.exit(app.exec())
