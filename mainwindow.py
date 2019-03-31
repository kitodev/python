# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from database import db_create

import sqlite3

class Ui_DataWindow(object):

    def db_load(self):
        conn = sqlite3.connect('mydb.db')
        query = "SELECT * FROM employees"
        result = conn.execute(query)
        self.tableWidget.setRowCount(0)
        for rowNumber, rowData in enumerate(result):
            self.tableWidget.insertRow(rowNumber)
            for colNumber, data in enumerate(rowData):
                self.tableWidget.setItem(rowNumber, colNumber, QtWidgets.QTable)

        conn.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Database Creator")
        MainWindow.resize(525, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.dblbl = QtWidgets.QLabel(self.splitter)
        self.dblbl.setObjectName("dblbl")
        self.createDatabase = QtWidgets.QLineEdit(self.splitter)
        self.createDatabase.setText("")
        self.createDatabase.setObjectName("createDatabase")
        self.createDbBtn = QtWidgets.QPushButton(self.splitter)
        self.createDbBtn.setObjectName("createDbBtn")
        self.loadDbBtn = QtWidgets.QPushButton(self.splitter)
        self.loadDbBtn.setObjectName("loadDbBtn")
        self.resultMsg = QtWidgets.QLabel(self.splitter)
        self.resultMsg.setText("")
        self.resultMsg.setObjectName("resultMsg")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.createDbBtn.clicked.connect(lambda : db_create(self.createDatabase.text()))
        self.loadDbBtn.clicked.connect(self.db_load)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Database Creator", "Database Creator"))
        self.dblbl.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Database Creator</span></p><p align=\"center\"><br/></p></body></html>"))
        self.createDatabase.setPlaceholderText(_translate("MainWindow", "Create Database"))
        self.createDbBtn.setText(_translate("MainWindow", "Create Database"))
        self.loadDbBtn.setText(_translate("MainWindow", "Load Databases"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataWindow = QtWidgets.QMainWindow()
    ui = Ui_DataWindow()
    ui.setupUi(DataWindow)
    DataWindow.show()
    sys.exit(app.exec_())