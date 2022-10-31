import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class WordFocus(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 50)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton(self)
        self.btn.move(132, 5)
        self.btn.resize(40, 40)
        self.btn.setText("->")
        self.btnpos = 0
        self.btn.clicked.connect(self.run)

        self.str1 = QLineEdit(self)
        self.str1.move(0, 15)

        self.str2 = QLineEdit(self)
        self.str2.move(171, 15)

    def run(self):
        if self.btnpos == 0:
            self.btnpos = 1
            self.btn.setText('<-')
            self.str2.setText(self.str1.text())
            self.str1.setText('')
        else:
            self.btnpos = 0
            self.btn.setText('->')
            self.str1.setText(self.str2.text())
            self.str2.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wf = WordFocus()
    wf.show()
    sys.exit(app.exec())
