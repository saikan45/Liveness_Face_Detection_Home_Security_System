# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memberwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import addmember
from time import sleep

class Ui_MemberWindow(object):
    
    def setupUi(self, MemberWindow):
        MemberWindow.setObjectName("MemberWindow")
        MemberWindow.resize(534, 772)
        self.centralwidget = QtWidgets.QWidget(MemberWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.name = QtWidgets.QTextEdit(self.centralwidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 3, 0, 1, 1)
        self.tphoto = QtWidgets.QPushButton(self.centralwidget)
        self.tphoto.setObjectName("tphoto")
        self.gridLayout.addWidget(self.tphoto, 4, 0, 1, 1)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/member/mem.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        MemberWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MemberWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        MemberWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MemberWindow)
        self.statusbar.setObjectName("statusbar")
        MemberWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MemberWindow)
        QtCore.QMetaObject.connectSlotsByName(MemberWindow)

        self.tphoto.clicked.connect(self.tphotobutton)
        self.close.clicked.connect(self.closebutton)

    def tphotobutton(self):
        font = QtGui.QFont()
        font.setPointSize(8)
        #self.open_window()
        self.label.setText("press s key to capture image and click close button to end the process")
        folder = self.name.toPlainText()
        try:
            path = 'C:/Users/soura/OneDrive/Desktop/HOme security system/program_files/face_dataset/'+folder
            os.mkdir(path)
        except:
           print("folder is already created")
        webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        sleep(2)
        while(webcam.isOpened()):
            for x in range(28):
                ret,frame = webcam.read()
                print(ret)
                print(frame)
                #path = 'D:/OpenCV/Scripts/Images'
                cv2.imshow("scanning",frame)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    cv2.imwrite(os.path.join(path , '0000'+str(x)+'.png'),frame)
                    self.label_2.setFont(font)
                    self.label_2.setText("image is saved in the location"+"C:/Users/soura/OneDrive/Desktop/HOme security system/program_files/face_dataset/"+folder)
                    font1 = QtGui.QFont()
                    font1.setPointSize(32)
                    self.name.setFont(font1)
                    self.name.setText("saved image with the name 0000"+str(x)+".png")
                elif key == ord('q'):
                    webcam.release()
                    #cv2.destroyAllWindows()
                    break
                    print("finished")
       

    def closebutton(self):
       #cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
       cv2.destroyAllWindows()
       MemberWindow.hide()

         

    def retranslateUi(self, MemberWindow):
        _translate = QtCore.QCoreApplication.translate
        MemberWindow.setWindowTitle(_translate("MemberWindow", "Add New Member"))
        self.tphoto.setText(_translate("MemberWindow", "submit and take photos"))
        self.close.setText(_translate("MemberWindow", "close"))
        self.label.setText(_translate("MemberWindow", "    Add Name and Photos Of New Member"))
        self.label_3.setText(_translate("MemberWindow", "Enter Name"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MemberWindow = QtWidgets.QMainWindow()
    ui = Ui_MemberWindow()
    ui.setupUi(MemberWindow)
    MemberWindow.show()
    sys.exit(app.exec_())
