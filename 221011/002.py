import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Минипланировщик"))
        self.pushButton.setText(_translate("MainWindow", "Добавить событие"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_event)

    def add_event(self):
        # получить описание
        description = self.lineEdit.text().strip()
        if description:
            # получить дату
            date = self.calendarWidget.selectedDate()
            # получить время
            time = self.timeEdit.time()
            res = f'{date.toPyDate()} {time.toString()} - {description}'
            # добавтиь
            self.listWidget.addItem(res)
            self.listWidget.sortItems()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
