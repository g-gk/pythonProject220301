import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Арифмометр')

        self.input1 = QLineEdit(self)
        self.input1.setFixedWidth(50)
        self.input1.setText('0')

        self.btn1 = QPushButton('+', self)
        self.btn1.setFixedWidth(30)

        self.btn2 = QPushButton('-', self)
        self.btn2.setFixedWidth(30)

        self.btn3 = QPushButton('*', self)
        self.btn3.setFixedWidth(30)

        self.input2 = QLineEdit(self)
        self.input2.setFixedWidth(50)
        self.input2.setText('0')

        self.btn1.move(50, 0)
        self.btn2.move(80, 0)
        self.btn3.move(110, 0)
        self.input2.move(140, 0)

        self.label1 = QLabel(self)
        self.label1.setText("=")
        self.label1.move(190, 5)

        self.input3 = QLineEdit(self)
        self.input3.setFixedWidth(50)
        self.input3.move(195, 0)
        self.input3.setText('0')
        self.input3.setEnabled(False)

        self.btn1.clicked.connect(self.a)
        self.btn2.clicked.connect(self.a)
        self.btn3.clicked.connect(self.a)

    def a(self):
        if self.sender() == self.btn1:
            try:
                v1 = int(self.input1.text())
                v2 = int(self.input2.text())
                res = v1 + v2
                self.input3.setText(str(res))
            except:
                self.input3.setText("Error")
        elif self.sender() == self.btn2:
            try:
                v1 = int(self.input1.text())
                v2 = int(self.input2.text())
                res = v1 - v2
                self.input3.setText(str(res))
            except:
                self.input3.setText("Error")
        elif self.sender() == self.btn3:
            try:
                v1 = int(self.input1.text())
                v2 = int(self.input2.text())
                res = v1 * v2
                self.input3.setText(str(res))
            except:
                self.input3.setText("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
