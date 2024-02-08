from functools import partial
from typing import List

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

from src.main.api.api import API
from src.main.view.qt_functions import create_push_button


class TeamSelector(QWidget):
    def __init__(self, api: API):
        super().__init__()
        self.init_ui(api)

    def init_ui(self, api: API):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

    def select_group(self, group_number):
        # TODO select group -> signal emit
        pass

    def refresh_ui(self, api: API):
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        width, height = api.calculate_view(api.get_number_of_groups())
        group_buttons: List[QPushButton] = []
        for group in range(0, api.get_number_of_groups()):
            group_buttons.append(create_push_button(str(group + 1), partial(self.select_group, group + 1)))
        for i in range(0, len(group_buttons)):
            self.grid.addWidget(group_buttons[i], i // width, i % width)