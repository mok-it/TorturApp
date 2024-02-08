from functools import partial

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.api.api import API
from src.main.view.qt_functions import create_push_button


class MenuBar(QWidget):

    signal = pyqtSignal(int)
    # 0 : back
    # 1 : search for name
    # 2 : rank
    # 3 : corrector
    # 4 : finish tortura

    def __init__(self, api: API):
        super().__init__()
        self.init_ui(api)

    def init_ui(self, api: API):
        grid = QGridLayout()

        self.back_button = create_push_button("Vissza", partial(self.change_widget, 0))
        self.name_finder_button = create_push_button("Keresés névre", partial(self.change_widget, 1))
        self.ranking_button = create_push_button("Tabella", partial(self.change_widget, 2))
        self.corrector_button = create_push_button("Javítás", partial(self.change_widget, 3))
        self.tortura_finisher_button = create_push_button("Tortúra befejezése", partial(self.change_widget, 4))

        grid.addWidget(self.back_button, 0, 0)
        if api.get_groups_file() != "":
            grid.addWidget(self.name_finder_button, 0, 1)
            grid.addWidget(self.ranking_button, 0, 2)
            grid.addWidget(self.corrector_button, 0, 3)
            grid.addWidget(self.tortura_finisher_button, 0, 4)
        else:
            grid.addWidget(self.ranking_button, 0, 1)
            grid.addWidget(self.corrector_button, 0, 2)
            grid.addWidget(self.tortura_finisher_button, 0, 3)
        self.setLayout(grid)

    def change_widget(self, code: int):
        self.signal.emit(code)
