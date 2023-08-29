from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QDialog, QHBoxLayout, QVBoxLayout, QListWidget)

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(500, 200)
        self.move(400, 400)
        self.setWindowTitle('To do List')

       
        self.tambahbtn = QPushButton('&ADD TASK')
        self.hapusbtn = QPushButton('&DELETE TASK')
        self.editbtn = QPushButton('&EDIT TASK')
        self.clrbtn = QPushButton('&CLEAR')

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.tambahbtn)
        button_layout.addWidget(self.hapusbtn)
        button_layout.addWidget(self.editbtn)
        button_layout.addWidget(self.clrbtn)
        button_layout.addStretch()
        self.contactList = QListWidget()

        main_layout = QHBoxLayout() 
        main_layout.addWidget(self.contactList)
        main_layout.addLayout(button_layout)  
        self.setLayout(main_layout)

        self.tambahbtn.clicked.connect(self.tambahbtnClick)
        self.hapusbtn.clicked.connect(self.hapusbtnClick)
        self.editbtn.clicked.connect(self.editbtnClick)
        self.clrbtn.clicked.connect(self.clrbtnClick)

        

        