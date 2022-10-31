from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel


class Flags(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('flag.ui', self)  # https://disk.yandex.ru/d/l7I1MWz_97LEGQ
        self.setWindowTitle('Текстовый флаг')
        self.buttonGroup.buttonClicked.connect(self.w)
        self.pushButton.clicked.connect(self.run)

    def w(self):
        self.s = (f'Цвета: {self.buttonGroup_3.checkedButton().text()}, '
                  f'{self.buttonGroup_2.checkedButton().text()} и '
                  f'{self.buttonGroup.checkedButton().text()}')

    def run(self):
        self.label_4.setText(self.s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Flags()
    ex.show()
    sys.exit(app.exec())
