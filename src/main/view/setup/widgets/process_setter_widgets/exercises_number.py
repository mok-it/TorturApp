from PyQt5.QtWidgets import QWidget, QGridLayout, QSpinBox

from src.main.view.qt_functions import create_label, create_spin_box


class ExercisesNumber(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.set_new_layout_with_widgets(5, False)

    def set_new_layout_with_widgets(self, number_of_blocks: int, custom: bool):
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        for i in range(number_of_blocks):
            self.grid.addWidget(create_label(str(i+1) + ". blokk"), i, 0)
            number_of_ex = create_spin_box(1, 10)
            number_of_ex.setValue(number_of_blocks - i)
            if custom:
                min_good_solution = create_spin_box(0, number_of_ex.value())
                number_of_ex.valueChanged.connect(self.change_min_good_sol)
                self.grid.addWidget(number_of_ex, i, 1)
                self.grid.addWidget(min_good_solution, i, 2)
            else:
                self.grid.addWidget(number_of_ex, i, 1)

    def change_min_good_sol(self):
        for i in range(0, self.grid.count(), 3):
            self.grid.itemAt(i+2).widget().setMaximum(self.grid.itemAt(i+1).widget().value())