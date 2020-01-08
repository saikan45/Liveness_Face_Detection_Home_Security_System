# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from adminone import Ui_AdminoneWindow
import adminresource
import cv2
import os

class Ui_AdminWindow(object):

    def open(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminoneWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(534, 772)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/admin/admin.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        #self.password = QtWidgets.QTextEdit(self.centralwidget)
        #self.password.setObjectName("password")
        #self.password.setCurrentCharFormat(QtWidgets.QLineEdit.Password)

        self.password =QtWidgets.QLineEdit(self.centralwidget)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.gridLayout.addWidget(self.password, 3, 0, 1, 1)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 5, 0, 1, 1)
        self.psubmit = QtWidgets.QPushButton(self.centralwidget)
        self.psubmit.setObjectName("psubmit")
        self.gridLayout.addWidget(self.psubmit, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

        self.psubmit.clicked.connect(self.psubmitbutton)
        self.close.clicked.connect(self.closebutton)

    def psubmitbutton(self):
       f=open("C:/Users/soura/OneDrive/Desktop/HOme security system/program_files/code.txt", "r")
       passtext = self.password.text()
       if f.mode == 'r':
        contents =f.read()
        print(contents)
       if contents == passtext:
        print("ok")
        self.open()
        self.label_4.setText("password matched")
       else:
        self.label_4.setText("wrong password")

    def closebutton(self):
        self.close()

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "AdminWindow"))
        self.label.setText(_translate("AdminWindow", "                Admin Panel"))
        self.close.setText(_translate("AdminWindow", "close"))
        self.psubmit.setText(_translate("AdminWindow", "submit"))
        self.label_3.setText(_translate("AdminWindow", "Enter Your Password Here:"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())
