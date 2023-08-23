from PyQt5.QtWidgets import (QWidget, QGridLayout, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250, 250)
        self.move(250, 300)
        self.setWindowTitle("Kalulator")

        self.lineEdit = QLineEdit
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit