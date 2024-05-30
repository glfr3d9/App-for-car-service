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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 495)
        self.label_name_tabel = QtWidgets.QLabel(Form)
        self.label_name_tabel.setObjectName("Автомобили")
        self.label_name_tabel.setStyleSheet(
            "background-color: #ffffff; color: #000000;border-style: solid; border-width: 1px; border-color: black;")
        self.label_name_tabel.setFont(QFont('Arial', 35))
        self.label_name_tabel.move(0, 0)
        self.label_name_tabel.resize(width / 3, height / 8)

        self.button_find = QtWidgets.QPushButton(Form)
        self.button_find.setObjectName("Поиск")
        self.button_find.setStyleSheet("background-color: #c0c0c0; color: #000000 ")
        self.button_find.setFont(QFont('Arial', 20))
        self.button_find.setGeometry(width / 3 + width / 4, 0, width / 8, height / 8)

        self.textbox_find = QtWidgets.QLineEdit(Form)
        self.textbox_find.move(width / 3, 0)
        self.textbox_find.resize(width / 4, height / 8)
        self.textbox_find.setStyleSheet("border : 1px black;border-style : solid;background-color: #ffffff;")
        self.textbox_find.setFont(QFont('Arial', 35))

        self.label_menu = QtWidgets.QLabel(Form)
        self.label_menu.setObjectName("Меню")
        self.label_menu.setStyleSheet("color: #000000;border-style: solid; border-width: 1px; border-color: black;")
        self.label_menu.setFont(QFont('Arial', 35))
        self.label_menu.move(width / 3 + width / 4 + width / 8, 0)
        self.label_menu.resize(width - (width / 3 + width / 4 + width / 8), height)
        self.label_menu.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.button_table_owner = QtWidgets.QPushButton(Form)
        self.button_table_owner.setObjectName("Клиенты")
        self.button_table_owner.setStyleSheet("background-color: #c0c0c0; color: #000000 ")
        self.button_table_owner.setFont(QFont('Arial', 20))
        self.button_table_owner.setGeometry(width / 3 + width / 4 + width / 8 + 50, height / 8 + 100,
                                            width - (width / 3 + width / 4 + width / 8) - 100, height / 8)

        self.button_table_car = QtWidgets.QPushButton(Form)
        self.button_table_car.setObjectName("Автомобиль")
        self.button_table_car.setStyleSheet("background-color: #c0c0c0; color: #000000 ")
        self.button_table_car.setFont(QFont('Arial', 20))
        self.button_table_car.setGeometry(width / 3 + width / 4 + width / 8 + 50, height / 8 * 2 + 150,
                                          width - (width / 3 + width / 4 + width / 8) - 100, height / 8)

        self.button_table_work = QtWidgets.QPushButton(Form)
        self.button_table_work.setObjectName("Отчеты")
        self.button_table_work.setStyleSheet("background-color: #c0c0c0; color: #000000 ")
        self.button_table_work.setFont(QFont('Arial', 20))
        self.button_table_work.setGeometry(width / 3 + width / 4 + width / 8 + 50, (height / 8) * 3 + 200,
                                           width - (width / 3 + width / 4 + width / 8) - 100, height / 8)

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(width/3,600,width - (width / 3 + width / 4 + width / 8) - 100, height / 8)
        self.pushButton_5.setStyleSheet("background-color: #c0c0c0; color: #000000 ")
        self.pushButton_5.setFont(QFont('Arial', 20))
        self.pushButton_5.setObjectName("Добавить")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(0,height / 8, width-(width - (width / 3 + width / 4 + width / 8)) ,500)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['Владелец', 'Модель', 'Марка ', 'госномер', 'VIN','масса','Радиус колеса'])


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name_tabel.setText(_translate("Form", "Автомобиль"))
        self.button_find.setText(_translate("Form", "Поиск"))
        self.label_menu.setText(_translate("Form", "Меню"))
        self.button_table_owner.setText(_translate("Form", "Клиенты"))
        self.button_table_car.setText(_translate("Form", "Автомобили"))
        self.button_table_work.setText(_translate("Form", "Отчеты"))
        self.pushButton_5.setText(_translate("Form", "Добавить"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())