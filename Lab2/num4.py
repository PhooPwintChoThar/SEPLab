import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class CurrencyConverter_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox=QVBoxLayout()
        self.label1=QLabel(self)
        self.label1.setText("Value")
        vbox.addWidget(self.label1)
        self.entry=QLineEdit(self)
        vbox.addWidget(self.entry)

     
        b2d=QPushButton("Baht to Dollar", self)
        b2d.clicked.connect(self.Baht2Dollar)
        vbox.addWidget(b2d)
        d2b=QPushButton("Dollar to Baht", self)
        d2b.clicked.connect(self.Dollar2Baht)
        vbox.addWidget(d2b)



        self.setLayout(vbox)
        self.show()

    def Baht2Dollar(self):

        baht=int(self.entry.text())
        dollar=baht/35
        dialog=QDialog(self)
        layout=QVBoxLayout()
        label=QLabel(self)
        t=str(baht)+ "bahts ="+str(dollar)+"dollars"
        label.setText(t)
        layout.addWidget(label)
        close_button=QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

    def Dollar2Baht(self):

        dollar=int(self.entry.text())
        baht=dollar * 35
        dialog=QDialog(self)
        layout=QVBoxLayout()
        label=QLabel(self)
        t=str(dollar)+"dollars ="+str(baht)+"bahts"
        label.setText(t)
        layout.addWidget(label)
        close_button=QPushButton("Close window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

    
if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=CurrencyConverter_window()
    sys.exit(app.exec())
