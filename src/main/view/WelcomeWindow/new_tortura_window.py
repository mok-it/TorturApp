from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.view.qt_functions import create_label, create_combo_box, create_push_button

class NewTorturaWindow(QWidget):
    clicked = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        camp_label = create_label("Tábor")
        age_label = create_label("Korcsoport")

        camp_list = ("Sástó 1", "Sástó 2", "Pusztafalu", "Pálköve 1", "Pálköve 2")
        camp_combobox = create_combo_box(camp_list)

        age_list = ("AB", "KLM", "PQRST", "XYZUp")
        age_combobox = create_combo_box(age_list)

        ok_button = create_push_button("OK", self.dummy_function)

        grid.addWidget(camp_label, 0, 0)
        grid.addWidget(camp_combobox, 0, 1)

        grid.addWidget(age_label, 1, 0)
        grid.addWidget(age_combobox, 1, 1)

        grid.addWidget(ok_button, 2, 0, 1, 2)

    def dummy_function(self):
        pass