from functools import partial

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.api.api import API
from src.main.view.qt_functions import create_label, create_combo_box, create_push_button


class CampAgeSetter(QWidget):

    signal = pyqtSignal(int)
    # 0 : back
    # 1 : forward

    def __init__(self, api: API):
        super().__init__()
        self.init_ui(api)

    def init_ui(self, api: API):
        grid = QGridLayout()

        self.camp_label = create_label("Tábor")
        # TODO read camps from config file
        self.camp_combobox = create_combo_box([])
        # TODO replace [] with the list of the camps

        self.age_label = create_label("Korcsoport")
        # TODO read ages from config file
        self.age_combo_box = create_combo_box([])
        # TODO replace [] with the list of the ages

        self.back_button = create_push_button("Vissza", self.go_back)
        self.ok_button = create_push_button("Tovább", partial(self.go_forward, api))

        grid.addWidget(self.camp_label, 0, 0)
        grid.addWidget(self.camp_combobox, 0, 1)
        grid.addWidget(self.age_label, 1, 0)
        grid.addWidget(self.age_combo_box, 1, 1)
        grid.addWidget(self.back_button, 2, 0)
        grid.addWidget(self.ok_button, 2, 1)

        self.setLayout(grid)

    def go_back(self):
        # TODO ??? save information from comboboxes and store them
        self.signal.emit(0)
        pass

    def go_forward(self, api: API):
        api.set_camp(self.camp_combobox.currentText())
        api.set_age(self.age_combo_box.currentText())
        self.signal.emit(1)
