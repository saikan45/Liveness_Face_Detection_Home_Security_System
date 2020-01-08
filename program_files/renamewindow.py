# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renamewindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
from reprocess import again
from batil import cancel


class Ui_RenameWindow(object):
    def setupUi(self, RenameWindow):
        RenameWindow.setObjectName("RenameWindow")
        RenameWindow.resize(435, 399)
        self.centralwidget = QtWidgets.QWidget(RenameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.newname = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newname.setFont(font)
        self.newname.setObjectName("newname")
        self.gridLayout.addWidget(self.newname, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.oldname = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oldname.setFont(font)
        self.oldname.setObjectName("oldname")
        self.gridLayout.addWidget(self.oldname, 2, 0, 1, 1)
        self.rename = QtWidgets.QPushButton(self.centralwidget)
        self.rename.setObjectName("rename")
        self.gridLayout.addWidget(self.rename, 5, 0, 1, 1)
        RenameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RenameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 26))
        self.menubar.setObjectName("menubar")
        RenameWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RenameWindow)
        self.statusbar.setObjectName("statusbar")
        RenameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RenameWindow)
        QtCore.QMetaObject.connectSlotsByName(RenameWindow)

        self.rename.clicked.connect(self.renamebutton)

    def renamebutton(self):
        path ='C:/Users/soura/OneDrive/Desktop/HOme security system/program_files/face_dataset/'
        oldtext = self.oldname.toPlainText()
        newtext = self.newname.toPlainText()
        oldpath = path+oldtext
        newpath = path+newtext
        print(oldpath)
        print("\n")
        print(newpath)
        again(oldtext,newtext)
        try:
            os.rename(oldpath,newpath)
            self.label.setText("successfully done")
        except:
            self.label.setText("Member Not found try again")
        
        

    def retranslateUi(self, RenameWindow):
        _translate = QtCore.QCoreApplication.translate
        RenameWindow.setWindowTitle(_translate("RenameWindow", "Rename Window"))
        self.label_3.setText(_translate("RenameWindow", "Enter New Name:"))
        self.label.setText(_translate("RenameWindow", "    Rename The Existing Member"))
        self.label_2.setText(_translate("RenameWindow", "Enter Old Name:"))
        self.rename.setText(_translate("RenameWindow", "Rename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RenameWindow = QtWidgets.QMainWindow()
    ui = Ui_RenameWindow()
    ui.setupUi(RenameWindow)
    RenameWindow.show()
    sys.exit(app.exec_())
