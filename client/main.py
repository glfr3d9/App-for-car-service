import Serv_book
import Main_page
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import socket

if __name__ == '__main__':
    app = QApplication(sys.argv)
    page = Main_page.Window()
    sock = socket.socket()
    sock.connect(('192.168.1.53', 10500))
    
    data = sock.recv(1024).decode()
    sock.close()
    serial = QSerialPort()
    serial.setBaudRate(115200)
    portList = []
    Num = 0
    ports = QSerialPortInfo().availablePorts()
    for port in ports:
        portList.append(port())
    self.tableWidget.setRowCount(0)
    for col_num, col_data in enumerate(record):
        self.tableWidget.insertColumn(col_num)
        for row_num, row_data in enumerate(record):
            self.tableWidget.insertRow(row_num)
            self.tableWidget.setItem(col_num, row_num, QTableWidgetItem(str(row_data)))
    sys.exit(app.exec_())


















