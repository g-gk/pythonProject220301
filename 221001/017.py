import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber


class chisla(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 420, 200)
        self.setWindowTitle('Вычисление выражений')

        self.btn = QPushButton('->', self)
        self.btn.resize(75, 75)
        self.btn.move(175, 50)
        self.btn.clicked.connect(self.vych)

        self.labelv = QLabel(self)
        self.labelv.setText("Первое число(целое)")
        self.labelv.move(10, 10)

        self.labelr = QLabel(self)
        self.labelr.setText('Второе число(целое)')
        self.labelr.move(10, 100)
        self.LCD_countpl = QLCDNumber(self)
        self.LCD_countpl.move(270, 20)
        self.LCD_countmin = QLCDNumber(self)
        self.LCD_countmin.move(270, 60)
        self.LCD_countumn = QLCDNumber(self)
        self.LCD_countumn.move(270, 100)
        self.LCD_countdel = QLCDNumber(self)
        self.LCD_countdel.move(270, 140)

        self.name_input = QLineEdit(self)
        self.name_input.resize(125, 25)
        self.name_input.move(10, 25)

        self.name_input1 = QLineEdit(self)
        self.name_input1.resize(125, 25)
        self.name_input1.move(10, 115)

    def vych(self):
        x = 0
        self.LCD_countpl.display(int(self.name_input.text()) + int(self.name_input1.text()))

        self.LCD_countmin.display(int(self.name_input.text()) - int(self.name_input1.text()))

        self.LCD_countumn.display(int(self.name_input.text()) * int(self.name_input1.text()))

        if self.name_input1.text != '0':
            self.LCD_countdel.display(
                round((int(self.name_input.text()) / int(self.name_input1.text())), 2))
        else:
            self.LCD_countdel.display('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chisla()
    ex.show()
    sys.exit(app.exec())
