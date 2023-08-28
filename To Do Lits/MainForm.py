from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QDialog, QHBoxLayout, QVBoxLayout, QListWidget)

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(500, 200)
        self.move(400, 200)
        self.setWindowTitle('To do List')

       
        self.tambahbtn = QPushButton('TAMBAH')
        self.hapusbtn = QPushButton('HAPUS')

        hbox = QHBoxLayout()
        hbox.addWidget(self.tambahbtn)
        hbox.addWidget(self.hapusbtn)

        self.contactList = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.contactList)
        layout.addLayout(hbox)
        self.setLayout(layout)
