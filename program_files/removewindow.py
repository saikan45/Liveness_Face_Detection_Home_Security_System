# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removewindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
from batil import cancel
class Ui_RemoveWindow(object):
    def setupUi(self, RemoveWindow):
        RemoveWindow.setObjectName("RemoveWindow")
        RemoveWindow.resize(312, 155)
        self.centralwidget = QtWidgets.QWidget(RemoveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.removetext = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.removetext.setFont(font)
        self.removetext.setObjectName("removetext")
        self.gridLayout.addWidget(self.removetext, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setObjectName("remove")
        self.gridLayout.addWidget(self.remove, 2, 0, 1, 1)
        RemoveWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RemoveWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 26))
        self.menubar.setObjectName("menubar")
        RemoveWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RemoveWindow)
        self.statusbar.setObjectName("statusbar")
        RemoveWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RemoveWindow)
        QtCore.QMetaObject.connectSlotsByName(RemoveWindow)

        self.remove.clicked.connect(self.removebutton)

    def removebutton(self):
       folder = self.removetext.toPlainText()
       path ='C:/Users/soura/OneDrive/Desktop/HOme security system/program_files/face_dataset/'+folder
       print(path)
       cancel(folder)
       try:
           #os.remove(path)
           shutil.rmtree(path)
           self.label.setText("successfully done")
       except:
           self.label.setText("Member not found try again")

    def retranslateUi(self, RemoveWindow):
        _translate = QtCore.QCoreApplication.translate
        RemoveWindow.setWindowTitle(_translate("RemoveWindow", "Remove Window"))
        self.label.setText(_translate("RemoveWindow", "Enter The Name To Remove:"))
        self.remove.setText(_translate("RemoveWindow", "Remove Member"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoveWindow = QtWidgets.QMainWindow()
    ui = Ui_RemoveWindow()
    ui.setupUi(RemoveWindow)
    RemoveWindow.show()
    sys.exit(app.exec_())
