# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camerawindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from take_photo import *
import cv2
import os
from time import sleep
from datetime import datetime
from observe import observevideo

class Ui_cameraWindow(object):


    def setupUi(self, cameraWindow):
        cameraWindow.setObjectName("cameraWindow")
        cameraWindow.resize(106, 176)
        self.centralwidget = QtWidgets.QWidget(cameraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 3, 0, 1, 1)

        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 5, 0, 1, 1)

        #self.button3 = QtWidgets.QPushButton(self.centralwidget)
        #self.button3.setObjectName("button3")
        #self.gridLayout.addWidget(self.button3, 2, 0, 1, 1)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)
        cameraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cameraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 26))
        self.menubar.setObjectName("menubar")
        cameraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cameraWindow)
        self.statusbar.setObjectName("statusbar")
        cameraWindow.setStatusBar(self.statusbar)

        self.retranslateUi(cameraWindow)
        QtCore.QMetaObject.connectSlotsByName(cameraWindow)
        
        self.label1.setText("enter shot to start and end to end the process")
        self.button1.clicked.connect(self.b1)
        self.button2.clicked.connect(self.b2)
        #self.button3.clicked.connect(self.b3)
    
    def b1(self):
        self.label1.setText("press s key to capture and q key to end the process")
        path = 'C:/Users/soura/OneDrive/Desktop/HOme security system/images'
        try:
            os.mkdir(path)
        except OSError:
            print("creating directory is failed")
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        sleep(2)
        while(cap.isOpened()):
            ret,frame = cap.read()
            cv2.imshow("press s key to capture and click end button to end the process",frame)
            key = cv2.waitKey(1)
            now = datetime.now()
            iname = now.strftime("%d%m%Y%H%M%S")
            #cv2.imwrite(os.path.join(path , 'photo'+'.jpg'),frame)
            if key == ord('s'):
                cv2.imwrite(os.path.join(path , 'photo'+'.jpg'),frame)
                print("captured")
                path1 = 'C:/Users/soura/OneDrive/Desktop/HOme security system/images/'+'photo.jpg'
                path3 = 'C:/Users/soura/OneDrive/Desktop/HOme security system/images/'+iname+'.jpg'
                os.rename(path1,path3)
                self.label2.setText("saved with name "+ iname)
            if key == ord('q'):
                #cv2.destroyAllWindows()
                #webcam.release()
                print("finished")
                break
        
        #cv2.destroyAllWindows()
    def b2(self):
        #cameraWindow.hide()
        cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
        #webcam.release()
        #self.hide()
        cv2.destroyAllWindows()

    def b3(self):
        observevideo()
          

    def retranslateUi(self, cameraWindow):
        _translate = QtCore.QCoreApplication.translate
        cameraWindow.setWindowTitle(_translate("cameraWindow", "camera_Window"))
        self.button1.setText(_translate("cameraWindow", "start"))
       # self.button2.setText(_translate("cameraWindow", "end"))
        #self.button3.setText(_translate("cameraWindow", "open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cameraWindow = QtWidgets.QMainWindow()
    ui = Ui_cameraWindow()
    ui.setupUi(cameraWindow)
    cameraWindow.show()
    sys.exit(app.exec_())
