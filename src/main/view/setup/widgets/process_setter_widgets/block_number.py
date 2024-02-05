from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout

from src.main.view.qt_functions import create_label, create_spin_box


class BlockNumber(QWidget):

    signal = pyqtSignal(int)
    # 0 : refresh exercise number widget UI

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        self.number_of_blocks_label = create_label("Blokkok száma")
        self.number_of_blocks_spinbox = create_spin_box(1, 10)
        self.number_of_blocks_spinbox.setValue(5)
        self.number_of_blocks_spinbox.valueChanged.connect(self.changed_block_number)

        grid.addWidget(self.number_of_blocks_label, 0, 0)
        grid.addWidget(self.number_of_blocks_spinbox, 0, 1)

        self.setLayout(grid)

    def changed_block_number(self):
        self.signal.emit(0)
