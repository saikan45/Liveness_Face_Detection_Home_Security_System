# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'securitywindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pi_face_recognition import runfunc
from liveness_demo import runlive
from commandwindow import Ui_AfterWindow
import security

class Ui_SecurityWindow(object):
    def openit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AfterWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, SecurityWindow):
        SecurityWindow.setObjectName("SecurityWindow")
        SecurityWindow.resize(534, 772)
        self.centralwidget = QtWidgets.QWidget(SecurityWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.match = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.match.setFont(font)
        self.match.setText("")
        self.match.setObjectName("match")
        self.gridLayout.addWidget(self.match, 4, 0, 1, 1)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/tala/security.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        SecurityWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecurityWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        SecurityWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecurityWindow)
        self.statusbar.setObjectName("statusbar")
        SecurityWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecurityWindow)
        QtCore.QMetaObject.connectSlotsByName(SecurityWindow)

        self.start.clicked.connect(self.startbutton)

    def startbutton(self):
       self.label.setText("press q key to remove the scanning frame")
       #num = runfunc("haarcascade_frontalface_default.xml","encodings.pickle")   
       num = runlive("liveness.model","le.pickle","face_detector")
       print(num)
       if(num == 1):
           self.label.setText("face matched")
           self.openit()
       else:
           self.label.setText("unrecognised face")
    def retranslateUi(self, SecurityWindow):
        _translate = QtCore.QCoreApplication.translate
        SecurityWindow.setWindowTitle(_translate("SecurityWindow", "Security Window"))
        self.start.setText(_translate("SecurityWindow", "Start"))
        self.label.setText(_translate("SecurityWindow", "            Security Panel "))
        self.close.setText(_translate("SecurityWindow", "close"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecurityWindow = QtWidgets.QMainWindow()
    ui = Ui_SecurityWindow()
    ui.setupUi(SecurityWindow)
    SecurityWindow.show()
    sys.exit(app.exec_())
