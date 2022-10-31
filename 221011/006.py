import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import difflib
import re

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMaximum(100.0)
        self.doubleSpinBox.setProperty("value", 50.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_2.addWidget(self.plainTextEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Антиплагиат v0.0001"))
        self.label.setText(_translate("MainWindow", "Порог срабатывания (%)"))
        self.label_2.setText(_translate("MainWindow", "Текст 1"))
        self.label_3.setText(_translate("MainWindow", "Текст 2"))
        self.pushButton.setText(_translate("MainWindow", "Сравнить"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.similarity)

    def prepate_text(self, text: str) -> str:
        res = ''
        # разбиваем на строки
        text_lines = text.split('\n')
        for text_line in text_lines:
            # удаление всех пробельных символов [\t\v\r\n\f]
            text_line = re.sub(r'\s+', '', text_line)
            res += text_line
        return res

    def similarity(self):
        text1 = self.plainTextEdit.toPlainText()
        text1 = self.prepate_text(text1)

        text2 = self.plainTextEdit_2.toPlainText()
        text2 = self.prepate_text(text2)

        seq = difflib.SequenceMatcher(a=text1.lower(), b=text2.lower())
        percent = seq.ratio() * 100

        self.statusBar.showMessage(f'Код похож на {percent:3.2f}%', 0)

        porog = self.doubleSpinBox.value()
        if percent > porog:
            self.statusBar.setStyleSheet("background-color : red")
        else:
            self.statusBar.setStyleSheet("background-color : green")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
