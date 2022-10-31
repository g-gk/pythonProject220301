import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Шестая программа')

        self.btn = QPushButton('<-', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 150)
        self.btn.clicked.connect(self.hello)

        self.name_input = QLineEdit(self)
        self.name_input.move(10, 150)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(230, 150)

    def hello(self):
        name = self.name_input.text()
        name2 = self.name_input2.text()
        self.name_input2.setText(name)
        self.name_input.setText(name2)

        if self.btn.text() == '->':
            self.btn.setText('<-')
        else:
            self.btn.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
