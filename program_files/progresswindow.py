# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progresswindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QTimer
from time import sleep
from encode_faces import runencode



class Ui_ProgWindow(object):
    def setupUi(self, ProgWindow):
        ProgWindow.setObjectName("ProgWindow")
        ProgWindow.resize(685, 229)
        self.centralwidget = QtWidgets.QWidget(ProgWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 3, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)
        ProgWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProgWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 26))
        self.menubar.setObjectName("menubar")
        ProgWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProgWindow)
        self.statusbar.setObjectName("statusbar")
        ProgWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProgWindow)
        QtCore.QMetaObject.connectSlotsByName(ProgWindow)

        self.timer = QTimer()    
        self.step =0

        self.label1.setText("Press the start button to train yout dataset")
        self.button1.clicked.connect(self.train)
        self.button1.clicked.connect(self.start)
        self.progressBar.setValue(0)
        
    def train(self):
        self.label2.setText("wait for a while")
        if self.step >= 10:
            self.timer.stop()
            return
        else:    
            while(self.step <=10):
                self.step += 0.000001
                #print(self.step)
                self.progressBar.setValue(self.step) 
        runencode("face_dataset","hog","encodings.pickle")  

    def restart(self):
        self.step = 0
        self.progressBar.setValue(0) 

    def start(self):
        self.timerEvent()
        if self.timer.isActive():
                self.timer.stop()
                self.button1.setText('Start')
        else:
            self.timer.start(100)
            self.button1.setText('Completed the task')
            self.label2.setText("Machine has been successfully trained")

    def timerEvent(self):
        if self.step >= 100:
            self.timer.stop()
            self.button1.setText('start')
            return
        else:    
            while(self.step <100):
                self.step += 0.00001
                #print(self.step)
                self.progressBar.setValue(self.step)          

    def retranslateUi(self, ProgWindow):
        _translate = QtCore.QCoreApplication.translate
        ProgWindow.setWindowTitle(_translate("ProgWindow", "Progress Window"))
        self.button1.setText(_translate("ProgWindow", "start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProgWindow = QtWidgets.QMainWindow()
    ui = Ui_ProgWindow()
    ui.setupUi(ProgWindow)
    ProgWindow.show()
    sys.exit(app.exec_())
