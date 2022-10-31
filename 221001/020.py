import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication


class Ariphmometr(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 320, 60)
        self.setWindowTitle('Арифмометр')

        self.input_val1 = QLineEdit(self)
        self.input_val1.move(10, 10)
        self.input_val1.resize(30, 30)

        self.input_val2 = QLineEdit(self)
        self.input_val2.move(150, 10)
        self.input_val2.resize(30, 30)

        self.rez = QLineEdit(self)
        self.rez.move(200, 10)
        self.rez.resize(30, 30)
        self.rez.setEnabled(False)

        self.plbtn = QPushButton('+', self)
        self.plbtn.resize(30, 30)
        self.plbtn.move(50, 10)
        self.plbtn.clicked.connect(self.pl)

        self.minbtn = QPushButton('-', self)
        self.minbtn.resize(30, 30)
        self.minbtn.move(80, 10)
        self.minbtn.clicked.connect(self.minu)

        self.umnbtn = QPushButton('*', self)
        self.umnbtn.resize(30, 30)
        self.umnbtn.move(110, 10)
        self.umnbtn.clicked.connect(self.umn)

    def pl(self):
        self.rez.setText(str(int(self.input_val1.text()) + int(self.input_val2.text())))

    def minu(self):
        self.rez.setText(str(int(self.input_val1.text()) - int(self.input_val2.text())))

    def umn(self):
        self.rez.setText(str(int(self.input_val1.text()) * int(self.input_val2.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ariphmometr()
    ex.show()
    sys.exit(app.exec())
