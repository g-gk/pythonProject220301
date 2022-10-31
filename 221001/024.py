import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.chb1 = QCheckBox('Чизбургер', self)
        self.chb1.move(10, 10)
        # self.chb1.stateChanged.connect(self.a)

        self.chb2 = QCheckBox('Гамбургер', self)
        self.chb2.move(10, 30)
        # self.chb2.stateChanged.connect(self.a)

        self.chb3 = QCheckBox('Кока-кола', self)
        self.chb3.move(10, 50)
        # self.chb3.stateChanged.connect(self.a)

        self.chb4 = QCheckBox('Нагетсы', self)
        self.chb4.move(10, 70)
        # self.chb4.stateChanged.connect(self.a)

        self.btn = QPushButton('Заказать', self)
        self.btn.setFixedWidth(80)
        self.btn.move(5, 100)
        self.btn.clicked.connect(self.a)

        self.tx = QPlainTextEdit(self)
        self.tx.move(5, 140)

        '''self.label1 = QLineEdit(self)
        self.label1.move(70, 10)'''

    def a(self):
        lb = 'Ваш заказ:\n\n'  # self.tx.toPlainText()
        if self.chb1.checkState():
            lb += self.chb1.text() + '\n'
        if self.chb2.checkState():
            lb += self.chb2.text() + '\n'
        if self.chb3.checkState():
            lb += self.chb3.text() + '\n'
        if self.chb4.checkState():
            lb += self.chb4.text() + '\n'
        self.tx.setPlainText(lb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
