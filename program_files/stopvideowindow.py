# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopvideowindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StopvideoWindow(object):
    def setupUi(self, StopvideoWindow):
        StopvideoWindow.setObjectName("StopvideoWindow")
        StopvideoWindow.resize(585, 149)
        self.centralwidget = QtWidgets.QWidget(StopvideoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        #self.button1 = QtWidgets.QPushButton(self.centralwidget)
        #self.button1.setObjectName("button1")
        #self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        StopvideoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StopvideoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 26))
        self.menubar.setObjectName("menubar")
        StopvideoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StopvideoWindow)
        self.statusbar.setObjectName("statusbar")
        StopvideoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StopvideoWindow)
        QtCore.QMetaObject.connectSlotsByName(StopvideoWindow)
        

    def retranslateUi(self, StopvideoWindow):
        _translate = QtCore.QCoreApplication.translate
        StopvideoWindow.setWindowTitle(_translate("StopvideoWindow", "video progess bar"))
        #self.button1.setText(_translate("StopvideoWindow", "stop recording"))
        self.label.setText(_translate("StopvideoWindow", "Your Video is recording , press q button  to stop and save your recording"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StopvideoWindow = QtWidgets.QMainWindow()
    ui = Ui_StopvideoWindow()
    ui.setupUi(StopvideoWindow)
    StopvideoWindow.show()
    sys.exit(app.exec_())
