from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout, QWidget
from src.main.view.qt_functions import create_push_button


class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        print(self.parentWidget())
        grid = QGridLayout()
        self.setLayout(grid)

        new_tortura_button = create_push_button("Új Tortúra", self.new_tortura)
        continue_tortura_button = create_push_button("Tortúra folytatása", self.continue_tortura)

        grid.addWidget(new_tortura_button, 0, 0)
        grid.addWidget(continue_tortura_button, 1, 0)

    def continue_tortura(self):
        pass

    def new_tortura(self):
        pass
