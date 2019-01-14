# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showTableList.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_ShowWindow(object):

    def setupUi(self, ShowWindow):
        ShowWindow.setObjectName("ShowWindow")
        ShowWindow.setFixedSize(808, 440)
        self.centralwidget = QtWidgets.QWidget(ShowWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 781, 371))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        lables = ['ID', 'Name', 'Index No.', 'Birthday', 'Address']
        self.tableWidget.setHorizontalHeaderLabels(lables)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(690, 385, 100, 29))
        self.showBtn.setObjectName("showBtn")
        ShowWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ShowWindow)
        self.statusbar.setObjectName("statusbar")
        ShowWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ShowWindow)
        QtCore.QMetaObject.connectSlotsByName(ShowWindow)

        self.loadData()
        self.showBtn.clicked.connect(self.loadData)

    def retranslateUi(self, ShowWindow):
        _translate = QtCore.QCoreApplication.translate
        self.showBtn.setText(_translate("MainWindow", "Reload"))
        ShowWindow.setWindowTitle(_translate("ShowWindow", "ShowWindow"))

    def loadData(self):
        try:
            conn = mysql.connector.connect(host='localhost', database='python_test_db', user='root', password='', use_pure=True)

            if conn.is_connected():

                sql = "SELECT `stu_id`, `name`, `index_no`, `birthday`, `address`  FROM `simple_table`"

                cursor = conn.cursor()
                cursor.execute(sql)
                records = cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(records):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                        
        except ConnectionError:
            print('Connection Error! ')

        except mysql.connector.Error as error:
            conn.rollback()
            print("connction failed {}".format(error))
        
        finally:
            if(conn.is_connected()):
                cursor.close()
                conn.close()
                print('Connection Closed')