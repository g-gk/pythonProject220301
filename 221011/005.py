import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxCountValue = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinBoxCountValue.sizePolicy().hasHeightForWidth())
        self.spinBoxCountValue.setSizePolicy(sizePolicy)
        self.spinBoxCountValue.setMinimum(5)
        self.spinBoxCountValue.setObjectName("spinBoxCountValue")
        self.horizontalLayout.addWidget(self.spinBoxCountValue)
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.horizontalLayout.addWidget(self.pushButtonStart)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate(
            "mainWindow", "Псевдоним. Возвращение"))
        self.label.setText(_translate(
            "mainWindow", "Задать количество камней"))
        self.pushButtonStart.setText(_translate("mainWindow", "Задать"))
        self.label_2.setText(_translate("mainWindow", "Сколько камней взять?"))
        self.pushButton_2.setText(_translate("mainWindow", "Взять"))


class MyWidget(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        Ui_mainWindow.setupUi(self, self)

        self.ostatok = 0
        self.pushButtonStart.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.step)

    def start(self):
        count = self.spinBoxCountValue.value()
        if not count:
            return
        # установить в остаток выбранное значение
        self.ostatok = count
        self.lcdNumber.display(self.ostatok)

        self.listWidget.clear()
        self.label_3.clear()

    def step(self):
        if self.ostatok <= 0:
            return
        # получить ход игрока
        player_step = self.spinBox_2.value()
        # если ход не корректный
        if player_step < 1 or player_step > 3 or player_step > self.ostatok:
            return
        self.ostatok -= player_step
        self.lcdNumber.display(self.ostatok)
        self.listWidget.addItem(f'Игрок взял - {player_step}')

        if not self.ostatok:
            # выводим что победил игрок
            self.label_3.setText('Победил игрок!')
            return

        # ИИ определяет сколько надо взять камней (1 или 2 или 3)
        if self.ostatok <= 1:  # если нет вариантов выиграть
            y = self.ostatok
        elif self.ostatok <= 4:  # если можно завершить с победой
            y = self.ostatok - 1  # делаем так чтобы у играка не было шансов
        else:  # например можно все время поддерживать сумму кратную 3 плюс 1
            y = self.ostatok % 4  # ход компьютера равен остатку от деления на 4
            if y == 0:  # если остаток равен 0 то берем остаток от деления на 3
                y = self.ostatok % 3
                if y == 0:  # если остаток равен 0 то берем остаток от деления на 2
                    y = self.ostatok % 2
                    if y == 0:
                        y = 1
        self.ostatok -= y  # остаток равен остаток минус ход ии
        self.lcdNumber.display(self.ostatok)
        self.listWidget.addItem(f'Компьютер взял - {y}')

        if not self.ostatok:
            # выводим что победил комп
            self.label_3.setText('Победил компьютер!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
