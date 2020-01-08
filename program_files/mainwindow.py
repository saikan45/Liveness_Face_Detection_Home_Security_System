# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mainresource
from adminwindow import Ui_AdminWindow
from securitywindow import Ui_SecurityWindow
from passwordwindow import Ui_PasswordWindow
from aboutwindow import Ui_AboutWindow
from helpwindow import Ui_HelpWindow
from observe import observevideo
from record_video import recording
from take_photo import photo
from camerawindow import Ui_cameraWindow
from stopvideowindow import Ui_StopvideoWindow
import cv2
class Ui_MainWindow(object):
    def openadminwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def opensecuritywindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecurityWindow()
        self.ui.setupUi(self.window)
        self.window.show()   

    def openpasswordwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PasswordWindow()
        self.ui.setupUi(self.window)
        self.window.show()   
    
    def openaboutwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()   

    def openhelpwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self.window)
        self.window.show()   

    def opencamerawindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_cameraWindow()
        self.ui.setupUi(self.window)
        self.window.show() 

    def openstopvideowindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StopvideoWindow()
        self.ui.setupUi(self.window)
        self.window.show()   

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.photo = QtWidgets.QPushButton(self.centralwidget)
        self.photo.setObjectName("photo")
        self.gridLayout.addWidget(self.photo, 3, 0, 1, 1)
        self.video = QtWidgets.QPushButton(self.centralwidget)
        self.video.setObjectName("video")
        self.gridLayout.addWidget(self.video, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap(":/mainlogo/logo.png"))
        self.label.setPixmap(QtGui.QPixmap("face"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setObjectName("exit")
        self.gridLayout.addWidget(self.exit, 5, 0, 1, 1)
        self.observe = QtWidgets.QPushButton(self.centralwidget)
        self.observe.setObjectName("observe")
        self.gridLayout.addWidget(self.observe, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        self.menuwindow = QtWidgets.QMenu(self.menubar)
        self.menuwindow.setObjectName("menuwindow")
        self.menusetting = QtWidgets.QMenu(self.menubar)
        self.menusetting.setObjectName("menusetting")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHome_window = QtWidgets.QAction(MainWindow)
        self.actionHome_window.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionHome_window.setObjectName("actionHome_window")
        self.actionsecurity_window = QtWidgets.QAction(MainWindow)
        self.actionsecurity_window.setObjectName("actionsecurity_window")
        self.actionadmin_window = QtWidgets.QAction(MainWindow)
        self.actionadmin_window.setObjectName("actionadmin_window")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionpassword_change = QtWidgets.QAction(MainWindow)
        self.actionpassword_change.setObjectName("actionpassword_change")
        self.actionabout_versions = QtWidgets.QAction(MainWindow)
        self.actionabout_versions.setObjectName("actionabout_versions")
        self.actionuser_manual = QtWidgets.QAction(MainWindow)
        self.actionuser_manual.setObjectName("actionuser_manual")
        self.menuwindow.addAction(self.actionHome_window)
        self.menuwindow.addAction(self.actionsecurity_window)
        self.menuwindow.addAction(self.actionadmin_window)
        self.menuwindow.addAction(self.actionexit)
        self.menusetting.addAction(self.actionpassword_change)
        self.menuabout.addAction(self.actionabout_versions)
        self.menuhelp.addAction(self.actionuser_manual)
        self.menubar.addAction(self.menuwindow.menuAction())
        self.menubar.addAction(self.menusetting.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionadmin_window.triggered.connect(lambda: self.openadminwindow())
        self.actionsecurity_window.triggered.connect(lambda: self.opensecuritywindow())
        self.actionpassword_change.triggered.connect(lambda: self.openpasswordwindow())
        self.actionabout_versions.triggered.connect(lambda: self.openaboutwindow())
        self.actionuser_manual.triggered.connect(lambda: self.openhelpwindow())
        self.actionexit.triggered.connect(lambda: self.close())

        self.observe.clicked.connect(self.observebutton)
        self.video.clicked.connect(self.videobutton)
        self.photo.clicked.connect(self.photobutton)
        self.exit.clicked.connect(self.exitbutton)
    
    def observebutton(self):
        observevideo()

    def videobutton(self):
        self.openstopvideowindow()
        recording()
        #print("ok")
    
    def photobutton(self):
        self.opencamerawindow() 
        #observevideo()


    def exitbutton(self):
            MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face_recognition_home_security_system"))
        self.photo.setText(_translate("MainWindow", "Take photo"))
        self.video.setText(_translate("MainWindow", "Record Video"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.observe.setText(_translate("MainWindow", "Observe"))
        self.label_2.setText(_translate("MainWindow", "   Face Recognition Home Security"))
        self.menuwindow.setTitle(_translate("MainWindow", "window"))
        self.menusetting.setTitle(_translate("MainWindow", "setting"))
        self.menuabout.setTitle(_translate("MainWindow", "about"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionHome_window.setText(_translate("MainWindow", "Home window"))
        self.actionHome_window.setStatusTip(_translate("MainWindow", "open home page"))
        self.actionHome_window.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionsecurity_window.setText(_translate("MainWindow", "security window"))
        self.actionsecurity_window.setStatusTip(_translate("MainWindow", "open security window"))
        self.actionsecurity_window.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionadmin_window.setText(_translate("MainWindow", "admin window"))
        self.actionadmin_window.setStatusTip(_translate("MainWindow", "open admin window"))
        self.actionadmin_window.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionexit.setStatusTip(_translate("MainWindow", "do exit"))
        self.actionexit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionpassword_change.setText(_translate("MainWindow", "password change"))
        self.actionpassword_change.setStatusTip(_translate("MainWindow", "open password change window"))
        self.actionpassword_change.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionabout_versions.setText(_translate("MainWindow", "about versions"))
        self.actionabout_versions.setStatusTip(_translate("MainWindow", "version window"))
        self.actionabout_versions.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionuser_manual.setText(_translate("MainWindow", "user manual"))
        self.actionuser_manual.setStatusTip(_translate("MainWindow", "open user manual"))
        self.actionuser_manual.setShortcut(_translate("MainWindow", "Ctrl+U"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
