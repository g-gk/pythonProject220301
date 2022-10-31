import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox

BYK = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w, h = 300, 100
        self.setGeometry(300, 300, w, h)
        self.setWindowTitle('Азбука Морзе 2')

        wb, hb = 20, 20
        xb, yb = 0, 0
        for b, z in BYK.items():
            btn = QPushButton(b.lower(), self)
            btn.setFixedSize(wb, hb)
            btn.move(xb, yb)
            btn.clicked.connect(self.a)
            xb += wb
            if xb > w - wb:
                xb = 0
                yb += hb

        self.label1 = QLineEdit(self)
        self.label1.setFixedWidth(w - wb)
        self.label1.move(0, yb + hb)

    def a(self):
        btn = self.sender()
        b = btn.text()
        c = self.label1.text()
        c += BYK[b.upper()]
        self.label1.setText(c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
