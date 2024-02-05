from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QRadioButton, QButtonGroup

from src.main.view.qt_functions import create_label, create_check_box, create_radio_button


class AdditionalSettings(QWidget):

    signal = pyqtSignal(int)
    # 0 : refresh exercise number widget UI

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        self.block_or_exercise_label = create_label("Blokkot vagy feladatot adunk ki?")
        self.boe_button_group = QButtonGroup()
        self.boe_block_radio_button = create_radio_button("Blokkot")
        self.boe_ex_radio_button = create_radio_button("Feladatot")
        self.boe_block_radio_button.setChecked(True)

        self.min_good_solution_label = create_label("Mennyi jó feladattól engedjük tovább a csapatokat?")
        self.mgs_button_group = QButtonGroup()
        self.mgs_fifty_plus_one_radio_button = create_radio_button("50% egész része + 1")
        self.mgs_fifty_radio_button = create_radio_button("50% egész része")
        self.mgs_custom_button = create_radio_button("Egyéni")
        self.mgs_fifty_plus_one_radio_button.setChecked(True)

        self.mgs_fifty_plus_one_radio_button.clicked.connect(self.custom_min_good_solution)
        self.mgs_fifty_radio_button.clicked.connect(self.custom_min_good_solution)
        self.mgs_custom_button.clicked.connect(self.custom_min_good_solution)

        self.custom_decision_checkbox = create_check_box("Tovább lehessen engedni csapatot manuálisan")

        grid.addWidget(self.block_or_exercise_label, 0, 0)
        grid.addWidget(self.boe_block_radio_button, 1, 0)
        grid.addWidget(self.boe_ex_radio_button, 2, 0)
        grid.addWidget(self.min_good_solution_label, 3, 0)
        grid.addWidget(self.mgs_fifty_plus_one_radio_button, 4, 0)
        grid.addWidget(self.mgs_fifty_radio_button, 5, 0)
        grid.addWidget(self.mgs_custom_button, 6, 0)
        grid.addWidget(self.custom_decision_checkbox, 7, 0)

        self.boe_button_group.addButton(self.boe_block_radio_button)
        self.boe_button_group.addButton(self.boe_ex_radio_button)

        self.mgs_button_group.addButton(self.mgs_fifty_plus_one_radio_button)
        self.mgs_button_group.addButton(self.mgs_fifty_radio_button)
        self.mgs_button_group.addButton(self.mgs_custom_button)

        self.setLayout(grid)

    def custom_min_good_solution(self):
        self.signal.emit(0)