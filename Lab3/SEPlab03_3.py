import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_Form

class TestUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.display=""
        
        self.ui.one.clicked.connect(self.display_value)
        self.ui.two.clicked.connect(self.display_value)
        self.ui.three.clicked.connect(self.display_value)
        self.ui.four.clicked.connect(self.display_value)
        self.ui.five.clicked.connect(self.display_value)
        self.ui.six.clicked.connect(self.display_value)
        self.ui.seven.clicked.connect(self.display_value)
        self.ui.eight.clicked.connect(self.display_value)
        self.ui.nine.clicked.connect(self.display_value)
        self.ui.zero.clicked.connect(self.display_value)
        self.ui.sharp.clicked.connect(self.display_value)
        self.ui.star.clicked.connect(self.display_value)
        self.ui.talk.clicked.connect(self.talk_num)
        self.ui.d.clicked.connect(self.clr)

    def display_value(self):
        btn=self.sender().text()
        self.display+=btn
        self.ui.display_text.setText(self.display)

    def clr(self):
        self.display=self.display[0:len(self.display)-1]
        self.ui.display_text.setText(self.display)

    
    def talk_num(self):
        label=f"Dialling << {self.display} >>"
        dialog=QDialog(self)
        lay=QVBoxLayout()
        l=QLabel(self)
        l.setText(label)
        lay.addWidget(l)
        close=QPushButton("End", self)
        close.clicked.connect(dialog.close)
        lay.addWidget(close)
        dialog.setLayout(lay)
        dialog.show()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=TestUI()
    w.show()
    sys.exit(app.exec())