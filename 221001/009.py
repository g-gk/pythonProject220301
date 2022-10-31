import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel, QLineEdit


class chisla(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 320, 80)
        self.setWindowTitle('Вычисление выражений')

        self.btn = QPushButton('->', self)
        self.btn.resize(25, 25)
        self.btn.move(150, 25)
        self.btn.clicked.connect(self.vych)

        self.labelv = QLabel(self)
        self.labelv.setText("Выражениe:")
        self.labelv.move(10, 10)

        self.labelr = QLabel(self)
        self.labelr.setText('Результат:')
        self.labelr.move(190, 10)

        self.name_input = QLineEdit(self)
        self.name_input.resize(125, 25)
        self.name_input.move(10, 25)

        self.name_input1 = QLineEdit(self)
        self.name_input1.resize(125, 25)
        self.name_input1.move(190, 25)

    def vych(self):
        chi = self.name_input.text()
        self.name_input1.setText(str(eval(chi)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chisla()
    ex.show()
    sys.exit(app.exec())
