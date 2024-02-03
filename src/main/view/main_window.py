from PyQt5.QtWidgets import QMainWindow, QApplication

from src.main.view.WelcomeWindow.welcome_window import WelcomeWindow
from src.main.view.WelcomeWindow.new_tortura_window import NewTorturaWindow
import sys
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 400, 284)
        self.setWindowTitle("Tortúra")
        self.init_ui()


    def init_ui(self):
        welcome_window = WelcomeWindow()
        new_tortura_window = NewTorturaWindow()

        self.setCentralWidget(welcome_window)

        welcome_window.new_tortura_signal.connect(partial(self.update_ui, new_tortura_window))

    def update_ui(self, widget):
        self.setCentralWidget(widget)

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


