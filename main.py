import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication
from sourav import Ui_MainWindow
stylesheet = """
    MainWindow {
        background-image: url("background.jpg");
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

def main():
    app = QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.resize(640, 600)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyleSheet(stylesheet)
    main_window.show()
    sys.exit(app.exec_())
main()
