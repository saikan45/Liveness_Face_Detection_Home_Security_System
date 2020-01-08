# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminone.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from memberwindow import Ui_MemberWindow
from renamewindow import Ui_RenameWindow
from removewindow import Ui_RemoveWindow
from encode_faces import runencode
from time import sleep
import adminoneresource
import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer
from progresswindow import Ui_ProgWindow



class Ui_AdminoneWindow(object):

    def open_member(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MemberWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_dorja(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ProgWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_rename(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RenameWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_remove(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RemoveWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, AdminoneWindow):
        AdminoneWindow.setObjectName("AdminoneWindow")
        AdminoneWindow.resize(534, 807)
        self.centralwidget = QtWidgets.QWidget(AdminoneWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/adminone/secu.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setObjectName("train")
        self.gridLayout.addWidget(self.train, 3, 0, 1, 1)
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setObjectName("remove")
        self.gridLayout.addWidget(self.remove, 5, 0, 1, 1)
        self.rename = QtWidgets.QPushButton(self.centralwidget)
        self.rename.setObjectName("rename")
        self.gridLayout.addWidget(self.rename, 4, 0, 1, 1)
        self.addmember = QtWidgets.QPushButton(self.centralwidget)
        self.addmember.setObjectName("addmember")
        self.gridLayout.addWidget(self.addmember, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 6, 0, 1, 1)
        AdminoneWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminoneWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        AdminoneWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminoneWindow)
        self.statusbar.setObjectName("statusbar")
        AdminoneWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminoneWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminoneWindow)

        self.addmember.clicked.connect(self.addmemberbutton)
        self.train.clicked.connect(self.trainbutton)
        self.rename.clicked.connect(self.renamebutton)
        self.remove.clicked.connect(self.removebutton)
        self.close.clicked.connect(self.closebutton)

    def renamebutton(self):
        self.open_rename()

    def trainbutton(self):
        #font = QtGui.QFont()
        #font.setPointSize(16)
        #self.label_2.setFont(font)
        self.open_dorja()
        #runencode("face_dataset","hog","encodings.pickle")  
       
        

    def addmemberbutton(self):
        self.open_member()

    def removebutton(self):
        self.open_remove()  

    def closebutton(self):
        self.close()


    def retranslateUi(self, AdminoneWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminoneWindow.setWindowTitle(_translate("AdminoneWindow", "Admin Panel"))
        self.train.setText(_translate("AdminoneWindow", "Train Dataset"))
        self.remove.setText(_translate("AdminoneWindow", "Remove Member"))
        self.rename.setText(_translate("AdminoneWindow", "Rename Member"))
        self.addmember.setText(_translate("AdminoneWindow", "Add New Member"))
        self.label.setText(_translate("AdminoneWindow", "                    Admin Panel"))
        self.close.setText(_translate("AdminoneWindow", "close"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminoneWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminoneWindow()
    ui.setupUi(AdminoneWindow)
    AdminoneWindow.show()
    sys.exit(app.exec_())
