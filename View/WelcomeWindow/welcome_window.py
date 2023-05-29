from View.qt_functions import *
from View.WelcomeWindow.new_tortura_window import NewTorturaWindow

class WelcomeWindow(QWidget):
    new_tortura_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print(self.parentWidget())
        grid = QGridLayout()
        self.setLayout(grid)

        new_tortura_button = createPushButton("Új Tortúra", self.newTortura)
        continue_tortura_button = createPushButton("Tortúra folytatása", self.dummy_function)


        grid.addWidget(new_tortura_button, 0, 0)
        grid.addWidget(continue_tortura_button, 1, 0)

    def dummy_function(self):
        pass

    def newTortura(self):
        self.new_tortura_signal.emit()
