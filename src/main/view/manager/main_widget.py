from PyQt5.QtWidgets import QWidget, QGridLayout


class ManagerMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        