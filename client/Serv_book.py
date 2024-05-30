from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sys
import mysql.connector
from mysql.connector import Error
import Main_page
import tkinter as tk
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
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("background-color: #c0c0c0;")
        self.tableWidget.setFont(QFont('Arial', 20))
        self.verticalLayout.addWidget(self.tableWidget)
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setObjectName("Состояниение автомобиля")
        self.button_back.setStyleSheet("background-color: #808080;")
        self.button_back.setFont(QFont('Arial', 40))
        self.button_back.clicked.connect(self.on_click_button_back)
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

        for col_num, col_data in enumerate(record):
            self.tableWidget.insertColumn(col_num)
            for row_num, row_data in enumerate(record):
                self.tableWidget.insertRow(row_num)
                self.tableWidget.setItem(col_num, row_num, QTableWidgetItem(str(row_data)))
        self.show()
    @pyqtSlot()
    data = ('''select gos_number, name_work, lastname, km, data from done_work
            inner join car on done_work.id_car=car.id inner join master
            on done_work.id_master = master.id)
            where gos_number =''')+filename.text()
    def on_click_button_back(self):
        self.ex = Main_page.Window()
        self.ex.show()
        self.close()