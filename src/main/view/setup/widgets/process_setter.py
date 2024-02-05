from functools import partial

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.api.api import API
from src.main.view.qt_functions import create_push_button
from src.main.view.setup.widgets.process_setter_widgets.additional_settings import AdditionalSettings
from src.main.view.setup.widgets.process_setter_widgets.block_number import BlockNumber
from src.main.view.setup.widgets.process_setter_widgets.exercises_number import ExercisesNumber


class ProcessSetter(QWidget):

    signal = pyqtSignal(int)
    # 0 : back
    # 1 : forward

    def __init__(self, api: API):
        super().__init__()
        self.init_ui(api)

    def init_ui(self, api: API):
        grid = QGridLayout()

        self.number_of_blocks = BlockNumber()
        self.exercises_number = ExercisesNumber()
        self.additinal_settings = AdditionalSettings()

        self.back_button = create_push_button("Vissza", self.go_back)
        self.ok_button = create_push_button("Tovább", partial(self.go_forward, api))

        grid.addWidget(self.number_of_blocks, 0, 0, 1, 1)
        grid.addWidget(self.exercises_number, 1, 0, 1, 1)
        grid.addWidget(self.additinal_settings, 0, 1, 2, 1)

        grid.addWidget(self.back_button, 2, 0, 1, 1)
        grid.addWidget(self.ok_button, 2, 1, 1, 1)

        self.setLayout(grid)

        self.additinal_settings.signal.connect(self.update_exercise_ui)
        self.number_of_blocks.signal.connect(self.update_exercise_ui)

    def update_exercise_ui(self, value):
        if value == 0:
            number_of_blocks = self.number_of_blocks.number_of_blocks_spinbox.value()
            custom_min_good = self.additinal_settings.mgs_custom_button.isChecked()
            self.exercises_number.set_new_layout_with_widgets(number_of_blocks, custom_min_good)

    def go_back(self):
        self.signal.emit(0)

    def go_forward(self, api: API):
        if self.additinal_settings.mgs_fifty_plus_one_radio_button.isChecked():
            api.set_blocks([self.exercises_number.grid.itemAt(i+1).widget().value()
                            for i in range(0, self.exercises_number.grid.count(), 2)],
                           0, [])
        elif self.additinal_settings.mgs_fifty_radio_button.isChecked():
            api.set_blocks([self.exercises_number.grid.itemAt(i+1).widget().value()
                            for i in range(0, self.exercises_number.grid.count(), 2)],
                           1, [])
        elif self.additinal_settings.mgs_custom_button.isChecked():
            api.set_blocks([self.exercises_number.grid.itemAt(i+1).widget().value()
                            for i in range(0, self.exercises_number.grid.count(), 3)],
                           0,
                           [self.exercises_number.grid.itemAt(i + 2).widget().value()
                            for i in range(0, self.exercises_number.grid.count(), 3)])
        self.signal.emit(1)
