# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commandwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import command

class Ui_AfterWindow(object):
    def setupUi(self, AfterWindow):
        AfterWindow.setObjectName("AfterWindow")
        AfterWindow.resize(534, 772)
        self.centralwidget = QtWidgets.QWidget(AfterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ok/okk.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.door = QtWidgets.QPushButton(self.centralwidget)
        self.door.setObjectName("door")
        self.gridLayout.addWidget(self.door, 3, 0, 1, 1)
        self.cdoor = QtWidgets.QPushButton(self.centralwidget)
        self.cdoor.setObjectName("cdoor")
        self.gridLayout.addWidget(self.cdoor, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.alarm = QtWidgets.QPushButton(self.centralwidget)
        self.alarm.setObjectName("alarm")
        self.gridLayout.addWidget(self.alarm, 5, 0, 1, 1)
        AfterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AfterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        AfterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AfterWindow)
        self.statusbar.setObjectName("statusbar")
        AfterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AfterWindow)
        QtCore.QMetaObject.connectSlotsByName(AfterWindow)

        self.door.clicked.connect(self.doorbutton)
        self.cdoor.clicked.connect(self.cdoorbutton)
        self.alarm.clicked.connect(self.alarmbutton)

    def doorbutton(self):
        self.label_3.setText("door is opened")
    def cdoorbutton(self):
        self.label_3.setText("door is closed")
    def alarmbutton(self):
        self.label_3.setText("alarm is on")

    def retranslateUi(self, AfterWindow):
        _translate = QtCore.QCoreApplication.translate
        AfterWindow.setWindowTitle(_translate("AfterWindow", "command Window"))
        self.label_2.setText(_translate("AfterWindow", "   Face Matched After recognition"))
        self.door.setText(_translate("AfterWindow", "Open The Door"))
        self.cdoor.setText(_translate("AfterWindow", "Close The Door"))
        self.label_3.setText(_translate("AfterWindow", "               Use The Following Buttons"))
        self.alarm.setText(_translate("AfterWindow", "Alarm"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AfterWindow = QtWidgets.QMainWindow()
    ui = Ui_AfterWindow()
    ui.setupUi(AfterWindow)
    AfterWindow.show()
    sys.exit(app.exec_())
