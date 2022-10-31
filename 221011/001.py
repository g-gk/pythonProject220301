import sys
import math

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(354, 575)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMinimumSize(QtCore.QSize(80, 80))
        self.table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setLineWidth(1)
        self.table.setMidLineWidth(1)
        self.table.setSmallDecimalPoint(False)
        self.table.setDigitCount(1)
        self.table.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        self.btn8.setMinimumSize(QtCore.QSize(80, 80))
        self.btn8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.digitbuttonGroup = QtWidgets.QButtonGroup(mainWindow)
        self.digitbuttonGroup.setObjectName("digitbuttonGroup")
        self.digitbuttonGroup.addButton(self.btn8)
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setMinimumSize(QtCore.QSize(80, 80))
        self.btn2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.digitbuttonGroup.addButton(self.btn2)
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_plus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.BinarybuttonGroup = QtWidgets.QButtonGroup(mainWindow)
        self.BinarybuttonGroup.setObjectName("BinarybuttonGroup")
        self.BinarybuttonGroup.addButton(self.btn_plus)
        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy)
        self.btn_eq.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_eq.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_eq.setFont(font)
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout.addWidget(self.btn_eq, 3, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        self.btn0.setMinimumSize(QtCore.QSize(80, 80))
        self.btn0.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.digitbuttonGroup.addButton(self.btn0)
        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_div.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.BinarybuttonGroup.addButton(self.btn_div)
        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.btn1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn1.setObjectName("btn1")
        self.digitbuttonGroup.addButton(self.btn1)
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        self.btn9.setMinimumSize(QtCore.QSize(80, 80))
        self.btn9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.digitbuttonGroup.addButton(self.btn9)
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_dot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 3, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setMinimumSize(QtCore.QSize(80, 80))
        self.btn3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.digitbuttonGroup.addButton(self.btn3)
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setMinimumSize(QtCore.QSize(80, 80))
        self.btn4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.digitbuttonGroup.addButton(self.btn4)
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setMinimumSize(QtCore.QSize(80, 80))
        self.btn5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.digitbuttonGroup.addButton(self.btn5)
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        self.btn7.setMinimumSize(QtCore.QSize(80, 80))
        self.btn7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.digitbuttonGroup.addButton(self.btn7)
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn6.setMinimumSize(QtCore.QSize(80, 80))
        self.btn6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.digitbuttonGroup.addButton(self.btn6)
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_minus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.BinarybuttonGroup.addButton(self.btn_minus)
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_mult.sizePolicy().hasHeightForWidth())
        self.btn_mult.setSizePolicy(sizePolicy)
        self.btn_mult.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_mult.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.BinarybuttonGroup.addButton(self.btn_mult)
        self.gridLayout.addWidget(self.btn_mult, 2, 3, 1, 1)
        self.btn_pow = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_pow.sizePolicy().hasHeightForWidth())
        self.btn_pow.setSizePolicy(sizePolicy)
        self.btn_pow.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_pow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.BinarybuttonGroup.addButton(self.btn_pow)
        self.gridLayout.addWidget(self.btn_pow, 4, 0, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_sqrt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 4, 1, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_fact.sizePolicy().hasHeightForWidth())
        self.btn_fact.setSizePolicy(sizePolicy)
        self.btn_fact.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_fact.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_fact.setFont(font)
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout.addWidget(self.btn_fact, 4, 2, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_clear.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(254, 166, 43);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 28))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate(
            "mainWindow", "Красивый калькулятор"))
        self.btn8.setText(_translate("mainWindow", "8"))
        self.btn2.setText(_translate("mainWindow", "2"))
        self.btn_plus.setText(_translate("mainWindow", "+"))
        self.btn_eq.setText(_translate("mainWindow", "="))
        self.btn0.setText(_translate("mainWindow", "0"))
        self.btn_div.setText(_translate("mainWindow", "/"))
        self.btn1.setText(_translate("mainWindow", "1"))
        self.btn9.setText(_translate("mainWindow", "9"))
        self.btn_dot.setText(_translate("mainWindow", "."))
        self.btn3.setText(_translate("mainWindow", "3"))
        self.btn4.setText(_translate("mainWindow", "4"))
        self.btn5.setText(_translate("mainWindow", "5"))
        self.btn7.setText(_translate("mainWindow", "7"))
        self.btn6.setText(_translate("mainWindow", "6"))
        self.btn_minus.setText(_translate("mainWindow", "-"))
        self.btn_mult.setText(_translate("mainWindow", "*"))
        self.btn_pow.setText(_translate("mainWindow", "^"))
        self.btn_sqrt.setText(_translate("mainWindow", "√"))
        self.btn_fact.setText(_translate("mainWindow", "!"))
        self.btn_clear.setText(_translate("mainWindow", "С"))


class MyWidget(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Загружаем дизайн
        # self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

        self.digitbuttonGroup.buttonClicked.connect(self.digitpress)
        self.BinarybuttonGroup.buttonClicked.connect(self.binnaroperpress)
        self.btn_eq.clicked.connect(self.enterpress)
        self.btn_clear.clicked.connect(self.clearpress)
        self.btn_sqrt.clicked.connect(self.sqrtpress)
        self.btn_dot.clicked.connect(self.dotpress)
        self.btn_fact.clicked.connect(self.factpress)

        self.operand1 = ""
        self.operand2 = "0"
        self.operaation = ""
        self.result = ""
        self.opperand2contentresult = False

    def calculate(self, expresion: str):
        self.opperand2contentresult = True
        try:
            self.operand2 = str(eval(expresion))
            if self.operand2.endswith('.0'):
                self.operand2 = self.operand2[:-2]
            self.table.setDigitCount(len(self.operand2))
            self.table.display(self.operand2)
        except Exception as e:
            print(self.operand1)
            print(e)
            self.operand2 = ''
            self.table.setDigitCount(len('ERROR'))
            self.table.display('ERROR')
        self.operand1 = ''

    def digitpress(self, btn):
        bt = btn.text()
        if self.opperand2contentresult:
            self.operand2 = bt
            self.opperand2contentresult = False
        else:
            if self.operand2 == '0':
                self.operand2 = bt
            else:
                self.operand2 += bt
        self.table.setDigitCount(len(self.operand2))
        self.table.display(self.operand2)

    def binnaroperpress(self, btn1):
        if self.operand2:
            if btn1.text() == '^':
                self.operand1 += self.operand2 + '**'
            else:
                self.operand1 += self.operand2 + btn1.text()
            self.operand2 = ""

    def enterpress(self):
        self.operand1 += self.operand2
        self.calculate(self.operand1)

    def clearpress(self):
        self.operand1 = ""
        self.operand2 = "0"
        self.table.setDigitCount(len(self.operand2))
        self.table.display(self.operand2)
        self.operand2 = ""

    def sqrtpress(self):
        self.operand1 = self.operand2 + '**0.5'
        self.calculate(self.operand1)

    def dotpress(self):
        btn = self.sender()
        bt = btn.text()
        if bt not in self.operand2 and not self.opperand2contentresult:
            if (len(self.operand2) > 0 and self.operand2[0] != "-") or (len(self.operand2) > 1):
                self.operand2 += bt
                self.table.setDigitCount(len(self.operand2))
                self.table.display(self.operand2)

    def factpress(self):
        x = float(self.operand2)
        if not x.is_integer():
            self.operand1 = 'ERROR'
        else:
            res = math.factorial(int(x))
            self.operand1 = str(res)
        self.calculate(self.operand1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
