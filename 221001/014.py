import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox

Morse_Dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
              'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
              'o': '---', 'p': '.--.', 'q': '--.-',
              'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..',
              ',': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', '0': '-----', '@': '.--.-.'}


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 150, 480, 130)
        self.setWindowTitle('Азбука Морзе 2')
        self.output = QLineEdit(self)
        self.output.move(0, 90)
        self.output.resize(480, 30)
        self.output.setEnabled(True)
        b = 0
        b1 = 0

        for k, v in Morse_Dict.items():
            self.btn = QPushButton(self)
            self.btn.setText(k)
            if b > 450:
                b = 0
                b1 += 30
            self.btn.resize(30, 30)
            self.btn.move(b, b1)
            b = b + 30
            self.btn.clicked.connect(self.run)

    def run(self):
        s = Morse_Dict[self.sender().text()]
        d = self.output.text()
        self.output.setText(f"{d} {s}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
