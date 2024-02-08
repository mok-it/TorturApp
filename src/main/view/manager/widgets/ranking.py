from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.api.api import API


class Ranking(QWidget):
    def __init__(self, api: API):
        super().__init__()
        self.init_ui(api)

    def init_ui(self, api: API):
        grid = QGridLayout()
        self.setLayout(grid)