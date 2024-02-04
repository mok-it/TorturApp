from PyQt5.QtWidgets import QMainWindow, QApplication

from src.main.view.manager.main_widget import ManagerMainWidget
from src.main.view.setup.main_widget import SetupMainWidget
from src.main.view.welcome_widget import WelcomeWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 400, 284)
        self.setWindowTitle("Tortúra")
        self.init_ui()

    def init_ui(self):
        welcome_widget = WelcomeWidget()
        manager_widget = ManagerMainWidget()
        setup_widget = SetupMainWidget()

        self.setCentralWidget(welcome_widget)

    def update_ui(self, widget):
        self.setCentralWidget(widget)


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
