# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import password

class Ui_PasswordWindow(object):
    def setupUi(self, PasswordWindow):
        PasswordWindow.setObjectName("PasswordWindow")
        PasswordWindow.resize(534, 936)
        self.centralwidget = QtWidgets.QWidget(PasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.newpassword = QtWidgets.QTextEdit(self.centralwidget)
        self.newpassword.setObjectName("newpassword")
        self.gridLayout.addWidget(self.newpassword, 5, 0, 1, 1)
        self.oldpassword = QtWidgets.QTextEdit(self.centralwidget)
        self.oldpassword.setObjectName("oldpassword")
        self.gridLayout.addWidget(self.oldpassword, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setObjectName("reset")
        self.gridLayout.addWidget(self.reset, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/chabi/pass.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.commentbox = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commentbox.setFont(font)
        self.commentbox.setText("")
        self.commentbox.setObjectName("commentbox")
        self.gridLayout.addWidget(self.commentbox, 7, 0, 1, 1)
        PasswordWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        PasswordWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordWindow)
        self.statusbar.setObjectName("statusbar")
        PasswordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(PasswordWindow)

        self.reset.clicked.connect(self.change_password)

    def change_password(self):
        f=open("code.txt", "r")
        if f.mode == 'r':
            contents =f.read()
            print(contents)
            newtext = self.newpassword.toPlainText()
            oldtext = self.oldpassword.toPlainText()
            
        if contents == oldtext:
            print("ok")
            contents = newtext
            f= open("code.txt","w+")
            f.write(contents)
            self.label.setText("successfully changed the password")
        else:
            print("vul code")
            self.label.setText("previous password doesn't missed")

    def retranslateUi(self, PasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        PasswordWindow.setWindowTitle(_translate("PasswordWindow", "Password Change Window"))
        self.label_3.setText(_translate("PasswordWindow", "Enter Your New PassWord:"))
        self.label.setText(_translate("PasswordWindow", "         Password Changing Panel"))
        self.label_2.setText(_translate("PasswordWindow", "Enter Your Old PassWord:"))
        self.reset.setText(_translate("PasswordWindow", "Reset Your Password"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordWindow = QtWidgets.QMainWindow()
    ui = Ui_PasswordWindow()
    ui.setupUi(PasswordWindow)
    PasswordWindow.show()
    sys.exit(app.exec_())
