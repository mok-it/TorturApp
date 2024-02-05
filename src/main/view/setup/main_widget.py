from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QStackedWidget

from src.main.api.api import API
from src.main.view.setup.widgets.camp_age_setter import CampAgeSetter
from src.main.view.setup.widgets.file_uploader import FileUploader
from src.main.view.setup.widgets.process_setter import ProcessSetter


class SetupMainWidget(QWidget):

    signal = pyqtSignal(int)
    # 0 : back
    # 2 : forward

    def __init__(self, api: API):
        super().__init__()
        self.init_ui(api)

    def init_ui(self, api: API):
        grid = QGridLayout()

        self.widgets = QStackedWidget()
        self.camp_age_setter = CampAgeSetter(api)
        self.process_setter = ProcessSetter(api)
        self.file_uploader = FileUploader(api)

        self.widgets.addWidget(self.camp_age_setter)
        self.widgets.addWidget(self.process_setter)
        self.widgets.addWidget(self.file_uploader)

        grid.addWidget(self.widgets, 0, 0)
        self.setLayout(grid)

        self.camp_age_setter.signal.connect(self.handle_camp_age_signal)
        self.process_setter.signal.connect(self.handle_process_setter_signal)
        self.file_uploader.signal.connect(self.handle_file_uploader_signal)

    def handle_camp_age_signal(self, value):
        if value == 0:
            self.signal.emit(0)
        elif value == 1:
            self.widgets.setCurrentWidget(self.process_setter)

    def handle_process_setter_signal(self, value):
        if value == 0:
            self.widgets.setCurrentWidget(self.camp_age_setter)
        elif value == 1:
            self.widgets.setCurrentWidget(self.file_uploader)

    def handle_file_uploader_signal(self, value):
        if value == 0:
            self.widgets.setCurrentWidget(self.process_setter)
        elif value == 1:
            self.signal.emit(2)
