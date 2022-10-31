import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.func = lambda x: x.show() if x.isHidden() else x.hide()

        self.cb1 = QCheckBox('edit1', self)
        self.cb2 = QCheckBox('edit2', self)
        self.cb3 = QCheckBox('edit3', self)
        self.cb4 = QCheckBox('edit4', self)

        self.name_input1 = QLineEdit(self)
        self.name_input2 = QLineEdit(self)
        self.name_input3 = QLineEdit(self)
        self.name_input4 = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 150, 300, 130)
        self.setWindowTitle('Прятки для виджетов')

        self.cb1.move(5, 10)
        self.cb1.stateChanged.connect(lambda: self.func(self.name_input1))
        self.name_input1.move(65, 10)

        self.cb2.move(5, 40)
        self.cb2.stateChanged.connect(lambda: self.func(self.name_input2))
        self.name_input2.move(65, 40)

        self.cb3.move(5, 70)
        self.cb3.stateChanged.connect(lambda: self.func(self.name_input3))
        self.name_input3.move(65, 70)

        self.cb4.move(5, 100)
        self.cb4.stateChanged.connect(lambda: self.func(self.name_input4))
        self.name_input4.move(65, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
