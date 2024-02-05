from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.api.api import API


class ManagerMainWidget(QWidget):
    def __init__(self, api: API):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        