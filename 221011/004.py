import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)

        self.items = [[1, 0, 1, 0],
                      [1, 1, 1],
                      [1, 0, 1],
                      [1, 0, 1],
                      ]
        for row_index in range(len(self.items)):
            row = self.items[row_index]
            for column_index in range(len(row)):
                btn = QtWidgets.QPushButton(self.centralwidget)
                btn_text = str(self.items[row_index][column_index])
                btn.setText(btn_text)
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                btn.setSizePolicy(sizePolicy)

                self.grid_layout.addWidget(btn, row_index, column_index)

        self.setCentralWidget(self.centralwidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
