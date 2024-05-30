from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Serv_book
import tkinter as tk
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1a1a1a;")
        self.setGeometry(0, 0, width, height)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.textbox = QTextEdit(self)
        self.label_consist_of_car = QLabel('Состояние автомобиля', self)
        self.initUI()
    def initUI(self):
        self.label_consist_of_car.setStyleSheet("color: #808080;")
        self.label_consist_of_car.setFont(QFont('Arial', 40))
        self.label_consist_of_car.move(width / 2 - 300, height / 13)
        self.label_consist_of_car.resize(width, 100)
        button_book = QPushButton('Сервисная книжка', self)
        button_book.setStyleSheet("background-color: #808080;")
        button_book.setFont(QFont('Arial', 20))
        button_book.setGeometry(0, height - height / 10, width - width / 6, height / 10)
        button_book.clicked.connect(self.on_click_button_book)
        button_exit = QPushButton('Выход', self)
        button_exit.setStyleSheet("background-color: #808080;")
        button_exit.setFont(QFont('Arial', 20))
        button_exit.setGeometry(width - width / 6, height - height / 10, width / 6, height / 10)
        button_exit.clicked.connect(self.on_click_button_exit)
        self.textbox.move(width / 8, height / 4)
        self.textbox.resize(width / 1.3, height / 2)
        self.textbox.setReadOnly(True)
        self.textbox.setStyleSheet("QTextEdit"
                                   "{"
                                   "border : 4px black;"
                                   "border-style : dotted;"
                                   "}")
        self.show()
    @pyqtSlot()
    def on_click_button_book(self):
        self.book = Serv_book.Ui_MainWindow()
        self.book.show()
    def on_click_button_exit(self):
        sys.exit(app.exec_())