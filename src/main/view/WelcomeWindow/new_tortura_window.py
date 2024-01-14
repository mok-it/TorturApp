from src.main.view.qt_functions import *

class NewTorturaWindow(QWidget):
    clicked = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        camp_label = createLabel("Tábor")
        age_label = createLabel("Korcsoport")

        camp_list = ("Sástó 1", "Sástó 2", "Pusztafalu", "Pálköve 1", "Pálköve 2")
        camp_combobox = createComboBox(camp_list)

        age_list = ("AB", "KLM", "PQRST", "XYZUp")
        age_combobox = createComboBox(age_list)

        ok_button = createPushButton("OK", self.dummy_function)

        grid.addWidget(camp_label, 0, 0)
        grid.addWidget(camp_combobox, 0, 1)

        grid.addWidget(age_label, 1, 0)
        grid.addWidget(age_combobox, 1, 1)

        grid.addWidget(ok_button, 2, 0, 1, 2)

    def dummy_function(self):
        pass