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

        self.lineEdit = QLineEdit()  # Inisialisasi objek dengan tanda kurung
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setFont(QFont('SansSerif', 14))
        self.lineEdit.setDisabled(True)
        self.lineEdit.setStyleSheet("background-color: lightgray;")

        self.__7btn = QPushButton('7')
        self.__8btn = QPushButton('8')
        self.__9btn = QPushButton('9')
        self.mulbtn = QPushButton('X')
        self.clearbtn = QPushButton('CLR')
        self.__4btn = QPushButton('4')
        self.__5btn = QPushButton('5')
        self.__6btn = QPushButton('6')
        self.divbtn = QPushButton('/')
        self.__1btn = QPushButton('1')
        self.__2btn = QPushButton('2')
        self.__3btn = QPushButton('3')
        self.__0btn = QPushButton('0')
        self.dotbtn = QPushButton('.')
        self.minusbtn = QPushButton('-')
        self.plusbtn = QPushButton('+')
        self.percentagebtn = QPushButton('%')
        self.calculatebtn = QPushButton('=')

        layout = QGridLayout()
        layout.addWidget(self.lineEdit, 0, 0, 1, 4)

        # Baris Pertama
        layout.addWidget(self.__7btn, 1, 0)
        layout.addWidget(self.__8btn, 1, 1)
        layout.addWidget(self.__9btn, 1, 2)
        layout.addWidget(self.clearbtn, 1, 3)

        # Baris Kedua
        layout.addWidget(self.__4btn,2, 0)
        layout.addWidget(self.__5btn,2, 1)
        layout.addWidget(self.__6btn,2, 2)
        layout.addWidget(self.mulbtn,2, 3)

        # Baris Ketiga
        layout.addWidget(self.__1btn,3,0)
        layout.addWidget(self.__2btn,3,1)
        layout.addWidget(self.__3btn,3,2)
        layout.addWidget(self.divbtn,3,3)

        # Baris keempat
        layout.addWidget(self.__0btn,4,0)
        layout.addWidget(self.dotbtn,4,1)
        layout.addWidget(self.minusbtn,4,2)
        layout.addWidget(self.plusbtn,4 ,3)

        # Baris Keempat
        layout.addWidget(self.percentagebtn,5,0)
        layout.addWidget(self.calculatebtn, 5, 1, 1, 3)
        self.setLayout(layout)

        self.__0btn.clicked.connect(lambda: self.writeDigit(0))
        self.__1btn.clicked.connect(lambda: self.writeDigit(1))
        self.__2btn.clicked.connect(lambda: self.writeDigit(2))
        self.__3btn.clicked.connect(lambda: self.writeDigit(3))
        self.__4btn.clicked.connect(lambda: self.writeDigit(4))
        self.__5btn.clicked.connect(lambda: self.writeDigit(5))
        self.__6btn.clicked.connect(lambda: self.writeDigit(6))
        self.__7btn.clicked.connect(lambda: self.writeDigit(7))
        self.__8btn.clicked.connect(lambda: self.writeDigit(8))
        self.__9btn.clicked.connect(lambda: self.writeDigit(9))
        self.dotbtn.clicked.connect(self.writePoint)
        self.mulbtn.clicked.connect(lambda: self.writeOperator('*'))
        self.divbtn.clicked.connect(lambda: self.writeOperator('/'))
        self.plusbtn.clicked.connect(lambda: self.writeOperator('+'))
        self.minusbtn.clicked.connect(lambda: self.writeOperator('-'))
        self.calculatebtn.clicked.connect(self.writeCalculate)
        self.percentagebtn.clicked.connect(self.percentagebtnClick)
        self.clearbtn.clicked.connect(self.lineEdit.clear)

    def writeDigit(self, digit):
        if digit in range(0,10):
            self.lineEdit.setText(
                self.lineEdit.text() + str(digit))

        
    def writePoint(self):
        if len(self.lineEdit.text()) == 0 or \
        self.lineEdit.text()[-1] in ['*', '/', '+', '-']:
            return
        self.lineEdit.setText(
            self.lineEdit.text() + '.')
    
        
    def writeOperator(self, operator):
        if len(self.lineEdit.text()) == 0: return
        if operator in ['*', '/', '+', '-']:
            if self.lineEdit.text()[-1] in ['*', '/', '+', '-']:
                self.lineEdit.setText(self.lineEdit.text()[-1] + operator)
            else:
                self.lineEdit.setText(self.lineEdit.text() + operator)

       
    def writeCalculate(self):
        expression = self.lineEdit.text()
        if len(expression)  == 0: return
        try:
            result = eval(expression)
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('ERROR')

    
       
    def percentagebtnClick(self):
        expression = self.lineEdit.text()
        if len(expression)  == 0: return
        try:
            result = eval(expression) / 100
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('ERROR')
    

        
