import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton('0', self)
        self.btn.resize(35, 25)
        self.btn.move(127, 103)
        self.btn.setText('->')
        self.btn.clicked.connect(self.count)

        self.name_input = QLineEdit(self)
        self.name_input.move(20, 105)
        self.name_input.setFixedSize(100, 20)

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(170, 105)
        self.name_input1.setFixedSize(100, 20)

    def count(self):
        if self.btn.text() == '->':
            name = self.name_input.text()
            self.name_input1.setText(name)
            self.name_input.setText('')
            self.btn.setText('<-')
        else:
            name = self.name_input1.text()
            self.name_input.setText(name)
            self.name_input1.setText('')
            self.btn.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
