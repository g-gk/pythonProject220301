import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 70)
        self.setWindowTitle('Вычисление выражений')

        self.input1 = QLineEdit(self)
        self.input1.setFixedWidth(100)

        self.btn = QPushButton('->', self)
        self.btn.setFixedWidth(30)

        self.input2 = QLineEdit(self)
        self.input2.setFixedWidth(100)

        w1 = self.input1.width()
        w2 = self.btn.width()

        self.input1.move(10, 30)
        self.btn.move(w1 + 10, 30)
        self.input2.move(w1 + w2 + 10, 30)
        self.btn.clicked.connect(self.a)

        self.label1 = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label1.setText("Выражение:")
        self.label1.move(10, 10)

        self.label2 = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label2.setText("Результат:")
        self.label2.move(w1 + w2 + 10, 10)

    def a(self):
        try:
            self.input2.setText(str(eval(self.input1.text())))
        except:
            self.input2.setText("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
