from src.main.view.qt_functions import *
from src.main.view.WelcomeWindow.welcome_window import WelcomeWindow
from src.main.view.WelcomeWindow.new_tortura_window import NewTorturaWindow
import sys
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 400, 284)
        self.setWindowTitle("Tortúra")
        self.initUI()


    def initUI(self):
        welcome_window = WelcomeWindow()
        new_tortura_window = NewTorturaWindow()

        self.setCentralWidget(welcome_window)

        welcome_window.new_tortura_signal.connect(partial(self.updateUI, new_tortura_window))

    def updateUI(self, widget):
        self.setCentralWidget(widget)

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


