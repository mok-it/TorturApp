import unittest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from src.main.view import qt_functions

app = QApplication(sys.argv)

class TestQtFunctions(unittest.TestCase):
    def test_createLabel(self):
        label = qt_functions.create_label("Test")
        self.assertIsInstance(label, QtWidgets.QLabel)
        self.assertEqual(label.text(), "Test")

if __name__ == '__main__':
    unittest.main()