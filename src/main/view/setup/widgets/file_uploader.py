from functools import partial

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QFileDialog, QMessageBox

from src.main.api.api import API
from src.main.view.qt_functions import create_label, create_push_button, create_message_box, create_spin_box


class FileUploader(QWidget):

    signal = pyqtSignal(int)
    # 0 : back
    # 1 : forward

    def __init__(self, api: API):
        super().__init__()
        self.groups_file_path: str = ""
        self.solutions_file_path: str = ""
        self.init_ui(api)

    def init_ui(self, api: API):
        grid = QGridLayout()

        self.group_number_label = create_label("Csapatok száma (ha nincs fájl)")
        self.group_number_spin_box = create_spin_box(1, 30)

        self.groups_label = create_label("Csapatok")
        self.groups_file_upload_button = create_push_button("Fájl feltöltése", self.upload_group_file)
        self.groups_selected_file_label = create_label("")

        self.solutions_label = create_label("Megoldások")
        self.solutions_file_upload_button = create_push_button("Fájl feltöltése", self.upload_solution_file)
        self.solutions_selected_file_label = create_label("")

        self.back_button = create_push_button("Vissza", self.go_back)
        self.ok_button = create_push_button("Tovább", partial(self.go_forward, api))

        grid.addWidget(self.group_number_label, 0, 0)
        grid.addWidget(self.group_number_spin_box, 0, 1)

        grid.addWidget(self.groups_label, 1, 0)
        grid.addWidget(self.groups_file_upload_button, 1, 1)
        grid.addWidget(self.groups_selected_file_label, 1, 2)

        grid.addWidget(self.solutions_label, 2, 0)
        grid.addWidget(self.solutions_file_upload_button, 2, 1)
        grid.addWidget(self.solutions_selected_file_label, 2, 2)

        grid.addWidget(self.back_button, 3, 0)
        grid.addWidget(self.ok_button, 3, 2)

        self.setLayout(grid)

    def upload_group_file(self, api: API):
        self.groups_upload_file_dialog = QFileDialog()
        self.groups_file_path, _ = QFileDialog.getOpenFileName()
        if self.groups_file_path:
            self.groups_selected_file_label.setText(self.groups_file_path)
            api.set_groups_file(self.groups_file_path)

    def upload_solution_file(self, api: API):
        self.solutions_upload_file_dialog = QFileDialog()
        self.solutions_file_path, _ = QFileDialog.getOpenFileName()
        if self.solutions_file_path:
            return_code = api.check_solution_file(self.solutions_file_path)
            if return_code == 0:
                self.solutions_selected_file_label.setText(self.solutions_file_path)
                api.set_solutions_file(self.solutions_file_path)
            elif return_code == 1:
                create_message_box("Hiba", "Nem megfelelő a megoldások száma! Ellenőrizd, hogy hány feladat van!", QMessageBox.Ok).show()
            elif return_code == 2:
                create_message_box("Hiba", "Ismeretlen hiba. Szólj Olivérnek vagy Ábelnek!", QMessageBox.Ok)

    def go_back(self):
        self.signal.emit(0)

    def go_forward(self, api):
        if self.groups_file_path:
            api.set_groups_file(self.groups_file_path)
        else:
            api.create_n_groups(self.group_number_spin_box.value())
        if self.solutions_file_path:
            api.set_solutions_file(self.solutions_file_path)
        self.signal.emit(1)
