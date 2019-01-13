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
        ShowWindow.resize(808, 417)
        self.centralwidget = QtWidgets.QWidget(ShowWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 781, 371))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(680, 350, 98, 29))
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

                sql = "SELECT * FROM `simple_table`"

                cursor = conn.cursor()
                cursor.execute(sql)
                records = cursor.fetchall()
                print(records)
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(records):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                        

        except mysql.connector.Error as error:
            conn.rollback()
            print("connction failed {}".format(error))
        
        finally:
            if(conn.is_connected()):
                cursor.close()
                conn.close()
                print('Connection Closed')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowWindow = QtWidgets.QMainWindow()
    ui = Ui_ShowWindow()
    ui.setupUi(ShowWindow)
    ShowWindow.show()
    sys.exit(app.exec_())