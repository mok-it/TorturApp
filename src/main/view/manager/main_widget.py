from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.api.api import API
from src.main.view.manager.widgets.corrector import Corrector
from src.main.view.manager.widgets.menubar import MenuBar
from src.main.view.manager.widgets.name_finder import NameFinder
from src.main.view.manager.widgets.ranking import Ranking
from src.main.view.manager.widgets.team_selector import TeamSelector
from src.main.view.manager.widgets.tortura_finisher import TorturaFinisher


class ManagerMainWidget(QWidget):
    def __init__(self, api: API):
        super().__init__()
        self.init_ui(api)

    def init_ui(self, api: API):
        grid = QGridLayout()

        self.menubar = MenuBar(api)
        self.team_selector = TeamSelector(api)
        self.other_widgets = QWidget()

        grid.addWidget(self.menubar, 0, 0, 1, 2)
        grid.addWidget(self.team_selector, 1, 0, 1, 1)
        grid.addWidget(self.other_widgets, 1, 1, 1, 1)

        self.setLayout(grid)

    def change_other_widget(self, value: int, api: API):
        if value == 0:
            # TODO signal emit
            pass
        elif value == 1:
            self.other_widgets = NameFinder(api)
        elif value == 2:
            self.other_widgets = Ranking(api)
        elif value == 3:
            self.other_widgets = Corrector(api)
        elif value == 4:
            self.other_widgets = TorturaFinisher(api)

        