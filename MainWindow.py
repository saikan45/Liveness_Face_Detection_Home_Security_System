from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QStatusBar
from PyQt5.uic import loadUi
from pi_face_recognition import runfunc

class MainWindow(QMainWindow):
    def __init__(self):
        WINDOW_TITLE = "Face_recognition_security_system"
        GUI_UI_LOCATION = "hello.ui"

        super(MainWindow, self).__init__()
        loadUi(GUI_UI_LOCATION, self)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Welcome")

        self.setWindowTitle(WINDOW_TITLE)
        # ^ Same ^
        
        self.button1.clicked.connect(self.face)
        self.button2.clicked.connect(self.train)

    def face(self):
        #self.mylabel.setText('hejdkslfj')
        #myfun('hello', 'test', 'bye')
        runfunc("haarcascade_frontalface_default.xml","encodings.pickle")

    def train(self)
        train(
