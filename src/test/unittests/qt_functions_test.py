import unittest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(parent_dir)
from main.view.qt_functions import create_label

app = QApplication(sys.argv)


class TestQtFunctions(unittest.TestCase):
    def test_createLabel(self):
        label = create_label("Test")
        self.assertIsInstance(label, QtWidgets.QLabel)
        self.assertEqual(label.text(), "Test")


if __name__ == '__main__':
    unittest.main()
