from typing import List, Callable

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QListWidget


def create_label(text: str) -> QtWidgets.QLabel:
    newlabel = QtWidgets.QLabel()
    newlabel.setText(text)
    newlabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    return newlabel


def create_push_button(text: str, function: Callable) -> QtWidgets.QPushButton:
    newpushbutton = QtWidgets.QPushButton()
    newpushbutton.setText(text)
    newpushbutton.clicked.connect(function)
    newpushbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    return newpushbutton


def create_line_edit() -> QtWidgets.QLineEdit:
    newlineedit = QtWidgets.QLineEdit()
    return newlineedit


def create_message_box(title: str, text: str, buttons) -> QtWidgets.QMessageBox:
    newmessagebox = QtWidgets.QMessageBox()
    newmessagebox.setWindowTitle(title)
    newmessagebox.setText(text)
    newmessagebox.setStandardButtons(buttons)
    return newmessagebox


def create_list_widget(title: str, function: Callable) -> QtWidgets.QListWidget:
    newlistwidget = QListWidget()
    newlistwidget.setWindowTitle(title)
    newlistwidget.itemDoubleClicked.connect(function)
    return newlistwidget


def create_spin_box(minv: int, maxv: int) -> QtWidgets.QSpinBox:
    newspinbox = QtWidgets.QSpinBox()
    newspinbox.setMinimum(minv)
    newspinbox.setMaximum(maxv)
    return newspinbox


def create_combo_box(lst: List) -> QtWidgets.QComboBox:
    combobox = QtWidgets.QComboBox()
    for x in lst:
        combobox.addItem(x)
    return combobox


def create_radio_button(radio_button_name) -> QtWidgets.QRadioButton:
    radio_button = QtWidgets.QRadioButton(radio_button_name)
    return radio_button


def create_check_box(label: str):
    return QtWidgets.QCheckBox(label)
