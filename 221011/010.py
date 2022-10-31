from random import choice

from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('randomstring.ui', self)  # https://disk.yandex.ru/d/mQybRCt7YbWAbw
        """Файл 'randomstring' нужно положить в ту же директорию, что и этот файл."""
        self.setWindowTitle('Случайная строка')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.s = ""
        f = open("lines.txt", "r")
        lines = f.readlines()
        if not bool(lines):
            pass
        else:
            self.s = choice(lines)[:-1]
        self.textBrowser.setText(self.s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec())
