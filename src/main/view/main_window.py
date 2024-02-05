from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

from src.main.api.api import API
from src.main.view.manager.main_widget import ManagerMainWidget
from src.main.view.setup.main_widget import SetupMainWidget
from src.main.view.welcome_widget import WelcomeWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self, api: API):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 400, 284)
        self.setWindowTitle("Tortúra")
        self.init_ui(api)

    def init_ui(self, api: API):
        self.widgets = QStackedWidget()

        self.welcome_widget = WelcomeWidget()
        self.manager_widget = ManagerMainWidget(api)
        self.setup_widget = SetupMainWidget(api)

        self.widgets.addWidget(self.welcome_widget)
        self.widgets.addWidget(self.manager_widget)
        self.widgets.addWidget(self.setup_widget)

        self.setCentralWidget(self.widgets)

        self.welcome_widget.signal.connect(self.update_ui)
        self.setup_widget.signal.connect(self.update_ui)

    def update_ui(self, value):
        if value == 0:
            self.widgets.setCurrentWidget(self.welcome_widget)
        elif value == 1:
            self.widgets.setCurrentWidget(self.setup_widget)
        elif value == 2:
            self.widgets.setCurrentWidget(self.manager_widget)


def window(api: API):
    app = QApplication(sys.argv)
    win = MainWindow(api)
    win.show()
    sys.exit(app.exec_())
