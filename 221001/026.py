from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

keys = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "CE", "+"],
    [".", "±", "="]
]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w, h = 250, 300
        x, y = 0, 0
        self.setGeometry(300, 300, w, h)
        self.setWindowTitle('Калькулятор')

        self.label1 = QLabel(self)
        self.label1.setFixedSize(w, 20)
        self.label1.move(x, y)
        self.label1.setAlignment(Qt.AlignRight)

        y += self.label1.height()

        self.label2 = QLabel(self)
        self.label2.setFixedSize(w, 20)
        self.label2.move(x, y)
        self.label2.setAlignment(Qt.AlignRight)
        f: QFont = self.label2.font()
        f.setPointSize(f.pointSize() + 10)
        self.label2.setFont(f)

        y += self.label2.height()
        bh = int((h - y) / len(keys))
        bw = int(w / len(keys[0]))
        btn = None
        for row in keys:
            x = 0
            for key in row:
                btn = QPushButton(key, self)
                btn.setFixedSize(bw, bh)
                btn.move(x, y)
                btn.clicked.connect(self.a)
                x += bw
            y += bh
        btn.setFixedWidth(bw * 2)

    def a(self):
        btn: QPushButton = self.sender()
        bt = btn.text()
        t1 = self.label1.text()
        t2 = self.label2.text()
        oper = ["+", "-", "*", "/"]
        if t2 == "ERROR":
            t2 = ""
        if bt in oper:
            if t2:
                t1 += t2 + bt
                t2 = ""
        elif bt == "=":
            t1 += t2
            try:
                t2 = str(eval(t1))
            except:
                t2 = "ERROR"
            t1 = ""
        elif bt == "CE":
            t2 = ""
        elif bt == "C":
            t1 = ""
            t2 = ""
        elif bt == ".":
            if bt not in t2:
                if (len(t2) > 0 and t2[0] != "-") or (len(t2) > 1):
                    t2 += bt
        elif bt == "±":
            if t2:
                if t2[0] == "-":
                    t2 = t2[1:]
                else:
                    t2 = "-" + t2
        else:
            if t2 != "0":
                t2 += bt
        self.label1.setText(t1)
        self.label2.setText(t2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
