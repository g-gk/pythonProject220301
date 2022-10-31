import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('Прятки для виджетов')

        self.chb1 = QCheckBox('edit1', self)
        self.chb1.move(10, 10)
        self.chb1.stateChanged.connect(self.a)

        self.chb2 = QCheckBox('edit2', self)
        self.chb2.move(10, 40)
        self.chb2.stateChanged.connect(self.a)

        self.chb3 = QCheckBox('edit3', self)
        self.chb3.move(10, 70)
        self.chb3.stateChanged.connect(self.a)

        self.chb4 = QCheckBox('edit4', self)
        self.chb4.move(10, 100)
        self.chb4.stateChanged.connect(self.a)

        self.label1 = QLineEdit(self)
        self.label1.move(70, 10)

        self.label2 = QLineEdit(self)
        self.label2.move(70, 40)

        self.label3 = QLineEdit(self)
        self.label3.move(70, 70)

        self.label4 = QLineEdit(self)
        self.label4.move(70, 100)

    def a(self):
        lb = None
        if self.sender() == self.chb1:
            lb = self.label1
        elif self.sender() == self.chb2:
            lb = self.label2
        elif self.sender() == self.chb3:
            lb = self.label3
        elif self.sender() == self.chb4:
            lb = self.label4
        if lb:
            if self.sender().checkState():
                lb.hide()
            else:
                lb.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
