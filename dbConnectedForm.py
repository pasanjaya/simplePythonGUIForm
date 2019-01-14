# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbConnectedForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from showTableList import Ui_ShowWindow

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 75, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 75, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 75, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 75, 21))
        self.label_4.setObjectName("label_4")
        self.nameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLine.setGeometry(QtCore.QRect(180, 80, 411, 29))
        self.nameLine.setObjectName("nameLine")
        self.indexNoLine = QtWidgets.QLineEdit(self.centralwidget)
        self.indexNoLine.setGeometry(QtCore.QRect(180, 120, 411, 29))
        self.indexNoLine.setObjectName("indexNoLine")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(180, 170, 411, 30))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2019, 12, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 210, 411, 70))
        self.textEdit.setObjectName("textEdit")
        self.submitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(490, 330, 98, 29))
        self.submitBtn.setObjectName("submitBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(370, 330, 98, 29))
        self.cancelBtn.setObjectName("cancelBtn")
        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(250, 330, 98, 29))
        self.showBtn.setObjectName("showBtn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 20, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submitBtn.clicked.connect(self.insertData)
        self.cancelBtn.clicked.connect(self.cancelClicked)
        self.showBtn.clicked.connect(self.loadData)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Index No"))
        self.label_3.setText(_translate("MainWindow", "Birthday"))
        self.label_4.setText(_translate("MainWindow", "Address"))
        self.submitBtn.setText(_translate("MainWindow", "Submit"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.showBtn.setText(_translate("MainWindow", "Show"))
        self.label_5.setText(_translate("MainWindow", "Simple Python/MySQL Form"))

    def cancelClicked(self):
        print('Cancel button clicked')
        exit()

    def loadData(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ShowWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def insertData(self):
        name = self.nameLine.text()
        index = self.indexNoLine.text()
        birthday = self.dateEdit.date().toPyDate()
        address = self.textEdit.toPlainText()

        try:
            conn = mysql.connector.connect(host='localhost', database='python_test_db', user='root', password='', use_pure=True)

            if conn.is_connected():
                db_info = conn.get_server_info()
                print('Connected, Info:', db_info)

                sql_insert_query = """ INSERT INTO `simple_table`
                          (`name`, `index_no`, `birthday`, `address`) VALUES (%s,%s,%s,%s)"""
                
                insert_data = (name, index, birthday, address)
                        
                cursor = conn.cursor(prepared=True)
                cursor.execute(sql_insert_query, insert_data)
                conn.commit()
                print('Data inserted')
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())