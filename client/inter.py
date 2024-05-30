from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import tkinter as tk
import mysql.connector
from mysql.connector import Error
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setGeometry(0, 0, width, height)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("background-color: #1a1a1a;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.label_consist_of_car = QtWidgets.QLabel(self.centralwidget)
        self.label_consist_of_car.setObjectName("Cервисная книжка")
        self.label_consist_of_car.setStyleSheet("color: #808080;")
        self.label_consist_of_car.setFont(QFont('Arial', 40))
        self.label_consist_of_car.resize(width, 100)
        self.label_consist_of_car.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_consist_of_car)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['госномер', 'название работы', 'Мастер', 'километраж', 'дата'])

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setStyleSheet("background-color: #c0c0c0;")
        self.tableWidget.setFont(QFont('Arial', 20))
        self.verticalLayout.addWidget(self.tableWidget)
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setObjectName("Состояниение автомобиля")
        self.button_back.setStyleSheet("background-color: #808080;")
        self.button_back.setFont(QFont('Arial', 40))
        #self.button_back.clicked.connect(self.on_click_button_back)
        self.verticalLayout.addWidget(self.button_back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_consist_of_car.setText(_translate("MainWindow", "Cервисная книжка"))
        self.button_back.setText(_translate("MainWindow", "Состояние автомобиля"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
