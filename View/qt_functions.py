from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from typing import List, Callable
from PyQt5.QtCore import pyqtSignal

def createLabel(text: str) -> QtWidgets.QLabel:
    newlabel = QtWidgets.QLabel()
    newlabel.setText(text)
    newlabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    return newlabel


def createPushButton(text: str, function: Callable) -> QtWidgets.QPushButton:
    newpushbutton = QtWidgets.QPushButton()
    newpushbutton.setText(text)
    newpushbutton.clicked.connect(function)
    newpushbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    return newpushbutton


def createLineEdit() -> QtWidgets.QLineEdit:
    newlineedit = QtWidgets.QLineEdit()
    return newlineedit


def createMessageBox(title: str, text: str, buttons) -> QtWidgets.QMessageBox:
    newmessagebox = QtWidgets.QMessageBox()
    newmessagebox.setWindowTitle(title)
    newmessagebox.setText(text)
    newmessagebox.setStandardButtons(buttons)
    return newmessagebox


def createListWidget(title: str, function: Callable) -> QtWidgets.QListWidget:
    newlistwidget = QListWidget()
    newlistwidget.setWindowTitle(title)
    newlistwidget.itemDoubleClicked.connect(function)
    return newlistwidget


def createSpinBox(minv: int, maxv: int) -> QtWidgets.QSpinBox:
    newspinbox = QtWidgets.QSpinBox()
    newspinbox.setMinimum(minv)
    newspinbox.setMaximum(maxv)
    return newspinbox

def createComboBox(lst: List) -> QtWidgets.QComboBox:
    combobox = QtWidgets.QComboBox()
    for x in lst:
        combobox.addItem(x)
    return combobox