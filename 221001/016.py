import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Вычисление выражений')

        self.input1 = QLineEdit(self)
        self.input1.setFixedWidth(100)

        self.btn = QPushButton('->', self)
        self.btn.setFixedWidth(50)

        self.input2 = QLineEdit(self)
        self.input2.setFixedWidth(100)

        w1 = self.input1.width()
        w2 = self.btn.width()

        self.input1.move(10, 30)
        self.btn.move(w1 + 20, 50)
        self.input2.move(10, 100)
        self.btn.clicked.connect(self.a)

        self.label1 = QLabel(self)
        self.label1.setText("Первое число(целое):")
        self.label1.move(10, 10)

        self.label2 = QLabel(self)
        self.label2.setText("Второе число(целое):")
        self.label2.move(10, 80)

        self.labelsum = QLabel(self)
        self.labelsum.setText("Сумма:")
        self.labelsum.move(220, 30)

        self.lcdsum = QLCDNumber(self)
        self.lcdsum.move(270, 30)

        self.labeldif = QLabel(self)
        self.labeldif.setText("Разность:")
        self.labeldif.move(210, 50)

        self.lcddif = QLCDNumber(self)
        self.lcddif.move(270, 50)

        self.labelmul = QLabel(self)
        self.labelmul.setText("Произведение:")
        self.labelmul.move(190, 70)

        self.lcdmul = QLCDNumber(self)
        self.lcdmul.move(270, 70)

        self.labeldiv = QLabel(self)
        self.labeldiv.setText("Частное:")
        self.labeldiv.move(210, 90)

        self.lcddiv = QLCDNumber(self)
        self.lcddiv.move(270, 90)

    def a(self):
        try:
            v1 = int(self.input1.text())
            v2 = int(self.input2.text())
            res = v1 + v2
            self.lcdsum.display(str(res))
        except:
            self.lcdsum.display("Error")

        try:
            v1 = int(self.input1.text())
            v2 = int(self.input2.text())
            res = v1 - v2
            self.lcddif.display(str(res))
        except:
            self.lcddif.display("Error")

        try:
            v1 = int(self.input1.text())
            v2 = int(self.input2.text())
            res = v1 * v2
            self.lcdmul.display(str(res))
        except:
            self.lcdmul.display("Error")

        try:
            v1 = int(self.input1.text())
            v2 = int(self.input2.text())
            res = v1 / v2
            self.lcddiv.display(f'{res:.3f}')
        except:
            self.lcddiv.display("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
