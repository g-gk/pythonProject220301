import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class Count(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 50)
        self.setWindowTitle('Вычисление выражений')

        self.btn = QPushButton(self)
        self.btn.move(132, 5)
        self.btn.resize(40, 40)
        self.btn.setText("->")
        self.btn.clicked.connect(self.run)

        self.str = QLineEdit(self)
        self.str.move(0, 15)

        self.res = QLineEdit(self)
        self.res.move(171, 15)

    def run(self):
        self.res.setText(str(eval(self.str.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cn = Count()
    cn.show()
    sys.exit(app.exec())
